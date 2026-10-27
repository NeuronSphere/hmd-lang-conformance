Using the vocabulary
====================

Everything runs in containers. The private index credential comes from the
keychain entry ``uv:hmdlabs.jfrog.io``.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Command
     - What it does
   * - ``make docker-test``
     - Installs the package and runs ``test/*.robot`` in a Python container.
   * - ``make docker-reqs-check``
     - Runs ``reqtrace`` in a Go container: every requirement tested, matrix current.
   * - ``make docker-render``
     - Regenerates ``src/python/hmd_lang_conformance`` from ``src/schemas`` in
       ``hmd-img-projectbuilder``.
   * - ``make conformance-image``
     - Builds ``hmd-ms-base-test`` with this vocabulary installed, tagged for a
       local nsctl deploy.

``hmd-entity-storage``'s conformance suites install this package in the Bender
container from ``test/test_requirements.txt``.
