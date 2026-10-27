#!/bin/sh
# Render hmd-lang-conformance's Python package (entity classes plus the
# <pkg>_client module hmd-ms-base's loader imports) through hmd-tmpl-vocabgen's
# python_lib and python_client templates, the way a lang pack's
# `hmd mickey build` does. src/schemas/ is the source of truth. The generated
# code, and a copy of the schemas the package ships, are committed under
# src/python/, so neither a service image nor the bender container needs mickey.
#
# Runs inside ghcr.io/hmdlabs/hmd-img-projectbuilder (make docker-render), with
#   /repo     = this repository
#   /vocabgen = an hmd-tmpl-vocabgen checkout (HMD_TMPL_VOCABGEN, default ../hmd-tmpl-vocabgen)
set -eu
# hmd-img-projectbuilder 0.5.395 pairs hmd-cli-mickey 1.0.52 with hmd-lib-mickey 0.1.3,
# which cannot import `clean` (HMD_LANG_CONFORMANCE_ISSUE_001); install a matching pair.
pip install -q --root-user-action=ignore "hmd-cli-mickey==${MICKEY_CLI_VERSION:-1.1.55}" \
  "hmd-lib-mickey==${MICKEY_LIB_VERSION:-0.2.85}" >/tmp/pip.log 2>&1 || { tail -5 /tmp/pip.log; exit 1; }
pkg=hmd_lang_conformance
schemas=/repo/src/schemas/$pkg
out=/repo/src/python/$pkg
work=/tmp/conformance-lang
rm -rf "$work" /tmp/hmd-tmpl-vocabgen /tmp/hmd-tmpl-vocabgen-hooks
mkdir -p "$work/meta-data" "$work/src/schemas"
cp -R "$schemas" "$work/src/schemas/$pkg"
cp -R /vocabgen/src/mickey/templates /tmp/hmd-tmpl-vocabgen
cp -R /vocabgen/src/mickey/hooks /tmp/hmd-tmpl-vocabgen-hooks
python - "$work/meta-data/manifest.json" "$pkg" <<'PY'
import json, sys
def gen(name, extra=None):
    cfg = json.load(open(f"/tmp/hmd-tmpl-vocabgen/{name}_config.json"))
    g = {
        "contexts": cfg["contexts"],
        "templates": cfg["templates"],
        "hooks": [h.replace("./src/mickey/hooks", "/tmp/hmd-tmpl-vocabgen-hooks") for h in cfg["hooks"]],
    }
    if extra:
        g["variables"] = extra
    return cfg, g
lib_cfg, lib = gen("python_lib")
_, client = gen("python_client", {"package_name": sys.argv[2], "base_package": sys.argv[2]})
manifest = {
    "name": "hmd-lang-conformance",
    "external_templates": ["/tmp/hmd-tmpl-vocabgen"],
    "contexts": lib_cfg["context_definitions"],
    "generate": {"python_lib": lib, "python_client": client},
}
json.dump(manifest, open(sys.argv[1], "w"), indent=2)
PY
cd "$work"
for target in python_lib python_client; do
  hmd mickey build "$target" -rp "$work" >/tmp/mickey.log 2>&1 || { cat /tmp/mickey.log; exit 1; }
done
# Replace the generated files and the packaged schema copy.
find "$out" -maxdepth 1 -name '*.py' -delete
cp "$work/src/python/$pkg/"*.py "$out/"
rm -rf "$out/schemas" && mkdir -p "$out/schemas" && cp -R "$schemas" "$out/schemas/$pkg"
ls "$out"
