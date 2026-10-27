.. hmd-lang-conformance requirements

Requirements
============

What the conformance vocabulary must provide, written as `sphinx-needs
<https://sphinx-needs.readthedocs.io/>`_ items so each one links to the tests that
verify it. The generated :doc:`traceability` page carries the matrix.

``hmd-lang-conformance`` is the shared test vocabulary for NERD005 (the Go
persistence stack, in ``hmd-entity-storage``): the Python and Go implementations
are both run against these nouns, so the vocabulary has to exercise every
``hmd-meta-types`` attribute type, required and optional.

How this works
--------------

**IDs** are area-coded::

    HMD_LANG_CONFORMANCE_REQ_<AREA>_<NNN>

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Area
     - Covers
   * - ``VOCAB``
     - What the nouns and relationships must contain.
   * - ``GEN``
     - The generated Python package.
   * - ``PKG``
     - Packaging, and the service image the conformance suites run against.

**Tests** live in ``test/*.robot`` and name the requirements they verify in
``[Tags]`` (short form ``REQ_<AREA>_<NNN>``). ``make docker-test`` runs them in a
Python container; ``make docker-reqs-check`` runs ``reqtrace`` in a Go container
and fails on an untested requirement, an untagged test, or a stale matrix. A
requirement no test in this repo can reach is tagged ``trace-exempt`` and its
text names what verifies it.

**Wording:** one RFC 2119 "shall" per requirement. IDs are never renumbered or
reused.

.. toctree::
   :maxdepth: 1

   vocabulary
   generated
   packaging
   traceability
