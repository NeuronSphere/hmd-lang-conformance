Generated package
=================

``src/schemas/`` is the source of truth. ``make docker-render`` regenerates the
Python package under ``src/python/hmd_lang_conformance/`` with
``hmd-tmpl-vocabgen``'s ``python_lib`` and ``python_client`` templates, and the
result is committed.

.. req:: The package ships the schemas unchanged
    :id: HMD_LANG_CONFORMANCE_REQ_GEN_001
    :status: implemented

    ``src/python/hmd_lang_conformance/schemas/hmd_lang_conformance/`` shall hold
    a byte-identical copy of every ``.hms`` file in
    ``src/schemas/hmd_lang_conformance/``, and no other file.

.. req:: Generated classes match their schemas
    :id: HMD_LANG_CONFORMANCE_REQ_GEN_002
    :status: implemented

    For every schema, the installed package shall provide a class whose
    ``entity_definition()`` equals the schema's JSON.

.. req:: A client module for hmd-ms-base's loader
    :id: HMD_LANG_CONFORMANCE_REQ_GEN_003
    :status: implemented

    The package shall provide ``hmd_lang_conformance.hmd_lang_conformance_client``
    with ``HmdLangConformanceClient`` and ``get_client_loader``, which
    ``hmd-ms-base``'s service loader imports for each lang pack named in
    ``loader_config``.
