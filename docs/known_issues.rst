Known issues in the Python implementation
#########################################

Concerns found in the Python toolchain this vocabulary depends on, recorded while
building it for NERD005 (``hmd-entity-storage``). Each has a stable ID.

Each entry is a sphinx-needs ``issue`` item, so it is in this repository's
``needs.json`` with its status, tags and links to the requirements it affects.
Status is one of: *open*; *fixed*; *deferred* (to the phase named);
*recorded-difference* (current behavior a requirement names, which the Go port
reproduces until Python and Go change together, NERD005 decisions 2 and 3); or
*go-difference* (the Go implementation differs on purpose). Entries tagged
``needs-decision`` wait on a decision from Brian or Alex.

.. needtable::
   :filter: type == "issue" and docname == "known_issues"
   :columns: id, title, status, tags
   :style: table
   :sort: id

.. issue:: hmd mickey build is broken in hmd-img-projectbuilder 0.5.395
   :id: HMD_LANG_CONFORMANCE_ISSUE_001
   :status: open
   :tags: bug, mickey, nerd005, toolchain

   :Summary: The projectbuilder image pairs hmd-cli-mickey 1.0.52 with hmd-lib-mickey 0.1.3, which fails with "cannot import name 'clean'", so no lang pack can render its code in the standard build image.
   :Where: ``tools/render.sh`` 13-16
   :Impact: Every lang pack's `hmd mickey build` fails in hmd-img-projectbuilder 0.5.395; this repo works around it by installing hmd-cli-mickey 1.1.55 and hmd-lib-mickey 0.2.85 from the private index before rendering.
   :Found by: Rendering this vocabulary for the NERD005 characterization, 2026-10-27; also NERD005 phase 2 (hmd-meta-types corpus).
   :Recommendation: Publish a projectbuilder image with a matching mickey CLI and library pair, then drop the workaround in tools/render.sh.

.. issue:: vocabgen's filter hook used a Jinja API removed in Jinja 3.1
   :id: HMD_LANG_CONFORMANCE_ISSUE_002
   :status: fixed
   :tags: bug, nerd005, toolchain, vocabgen

   :Summary: hmd-tmpl-vocabgen's filter hook imported jinja2.contextfilter, which Jinja 3.1 removed, so no vocabgen template rendered in the current toolchain.
   :Where: ``hmd-tmpl-vocabgen`` ``src/mickey/hooks``
   :Impact: All vocabgen-based code generation (python_lib, python_client, go_lib, typescript_lib) failed for every lang pack.
   :Found by: NERD005 phase 2 (go_lib corpus), 2026-10-26.
   :Fixed in: hmd-tmpl-vocabgen b1b0405
   :Recommendation: Done: the hook imports pass_context. Rebuild lang packs that pinned an older vocabgen.

.. issue:: Not yet published: consumers install from git
   :id: HMD_LANG_CONFORMANCE_ISSUE_003
   :status: open
   :tags: nerd005, packaging

   :Summary: hmd-lang-conformance is not on the private index yet, so hmd-entity-storage's Bender container installs it from the GitHub repository's src/python subdirectory.
   :Where: ``src/python/setup.py`` 1
   :Impact: Conformance runs need GitHub access from the Bender container (and credentials if the repository is private), and they track main rather than a released version.
   :Found by: Moving the vocabulary out of hmd-entity-storage, 2026-10-27.
   :Recommendation: Publish 0.1.0 to the private index with `hmd build` and pin hmd-lang-conformance~=0.1 in hmd-entity-storage/test/test_requirements.txt.

.. issue:: Lang packs must be baked into the service image
   :id: HMD_LANG_CONFORMANCE_ISSUE_004
   :status: open
   :tags: design, hmd-ms-base, nerd005
   :links: HMD_LANG_CONFORMANCE_REQ_PKG_002

   :Summary: hmd-ms-base loads a lang pack by importing it, so serving this vocabulary needs a derived hmd-ms-base-test image with the package pip-installed rather than configuration alone.
   :Where: ``docker/Dockerfile.ms-base-test`` 1
   :Impact: Every vocabulary change needs an image rebuild and a redeploy; a local nsctl environment also needs the image tagged under the bare and registry-qualified names.
   :Found by: NERD005 characterization on scratch, 2026-10-27.
   :Recommendation: Consider runtime lang-pack installation (or a lang-pack volume) in hmd-ms-base, and in the Go ms-base from the start.

.. issue:: No Go code is generated for the vocabulary yet
   :id: HMD_LANG_CONFORMANCE_ISSUE_005
   :status: deferred
   :tags: go, nerd005

   :Summary: Only the Python package is generated; the go_lib template (fixed in hmd-tmpl-vocabgen b1b0405) is not yet run for this vocabulary, and go_lib does not emit a go.mod.
   :Where: ``tools/render.sh`` 1
   :Impact: The Go CRUD service and Go engines (NERD005 phase 3 onward) cannot use these nouns until Go code is generated and importable.
   :Found by: NERD005 phase 2 report, 2026-10-26.
   :Deferred to: NERD005 phase 3
   :Recommendation: Add go_lib to tools/render.sh, commit src/go with a go.mod, and tag src/go/<module>/v0.1.0.
