Known issues in the Python implementation
#########################################

Concerns found in the Python toolchain this vocabulary depends on, recorded while
building it for NERD005 (``hmd-entity-storage``). Each has a stable ID. Status is one of:
*open*; *fixed in <commit>*; *deferred to NERD005 phase N*; or *recorded difference*.

.. _HMD_LANG_CONFORMANCE_ISSUE_001:

HMD_LANG_CONFORMANCE_ISSUE_001: hmd mickey build is broken in hmd-img-projectbuilder 0.5.395
============================================================================================

:Summary: The projectbuilder image pairs hmd-cli-mickey 1.0.52 with hmd-lib-mickey 0.1.3, which fails with "cannot import name 'clean'", so no lang pack can render its code in the standard build image.
:Where: ``tools/render.sh`` 13-16
:Impact: Every lang pack's `hmd mickey build` fails in hmd-img-projectbuilder 0.5.395; this repo works around it by installing hmd-cli-mickey 1.1.55 and hmd-lib-mickey 0.2.85 from the private index before rendering.
:Found by: Rendering this vocabulary for the NERD005 characterization, 2026-10-27; also NERD005 phase 2 (hmd-meta-types corpus).
:Status: open
:Recommendation: Publish a projectbuilder image with a matching mickey CLI and library pair, then drop the workaround in tools/render.sh.

.. _HMD_LANG_CONFORMANCE_ISSUE_002:

HMD_LANG_CONFORMANCE_ISSUE_002: vocabgen's filter hook used a Jinja API removed in Jinja 3.1
============================================================================================

:Summary: hmd-tmpl-vocabgen's filter hook imported jinja2.contextfilter, which Jinja 3.1 removed, so no vocabgen template rendered in the current toolchain.
:Where: ``hmd-tmpl-vocabgen`` ``src/mickey/hooks``
:Impact: All vocabgen-based code generation (python_lib, python_client, go_lib, typescript_lib) failed for every lang pack.
:Found by: NERD005 phase 2 (go_lib corpus), 2026-10-26.
:Status: fixed in hmd-tmpl-vocabgen b1b0405
:Recommendation: Done: the hook imports pass_context. Rebuild lang packs that pinned an older vocabgen.

.. _HMD_LANG_CONFORMANCE_ISSUE_003:

HMD_LANG_CONFORMANCE_ISSUE_003: Not yet published: consumers install from git
=============================================================================

:Summary: hmd-lang-conformance is not on the private index yet, so hmd-entity-storage's Bender container installs it from the GitHub repository's src/python subdirectory.
:Where: ``src/python/setup.py`` 1
:Impact: Conformance runs need GitHub access from the Bender container (and credentials if the repository is private), and they track main rather than a released version.
:Found by: Moving the vocabulary out of hmd-entity-storage, 2026-10-27.
:Status: open
:Recommendation: Publish 0.1.0 to the private index with `hmd build` and pin hmd-lang-conformance~=0.1 in hmd-entity-storage/test/test_requirements.txt.

.. _HMD_LANG_CONFORMANCE_ISSUE_004:

HMD_LANG_CONFORMANCE_ISSUE_004: Lang packs must be baked into the service image
===============================================================================

:Summary: hmd-ms-base loads a lang pack by importing it, so serving this vocabulary needs a derived hmd-ms-base-test image with the package pip-installed rather than configuration alone.
:Where: ``docker/Dockerfile.ms-base-test`` 1
:Impact: Every vocabulary change needs an image rebuild and a redeploy; a local nsctl environment also needs the image tagged under the bare and registry-qualified names.
:Found by: NERD005 characterization on scratch, 2026-10-27.
:Status: open
:Recommendation: Consider runtime lang-pack installation (or a lang-pack volume) in hmd-ms-base, and in the Go ms-base from the start.

.. _HMD_LANG_CONFORMANCE_ISSUE_005:

HMD_LANG_CONFORMANCE_ISSUE_005: No Go code is generated for the vocabulary yet
==============================================================================

:Summary: Only the Python package is generated; the go_lib template (fixed in hmd-tmpl-vocabgen b1b0405) is not yet run for this vocabulary, and go_lib does not emit a go.mod.
:Where: ``tools/render.sh`` 1
:Impact: The Go CRUD service and Go engines (NERD005 phase 3 onward) cannot use these nouns until Go code is generated and importable.
:Found by: NERD005 phase 2 report, 2026-10-26.
:Status: deferred to NERD005 phase 3
:Recommendation: Add go_lib to tools/render.sh, commit src/go with a go.mod, and tag src/go/<module>/v0.1.0.
