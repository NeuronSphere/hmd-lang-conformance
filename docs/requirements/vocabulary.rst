Vocabulary
==========

.. req:: Every type, required
    :id: HMD_LANG_CONFORMANCE_REQ_VOCAB_001
    :status: implemented

    The noun ``hmd_lang_conformance.typed_required`` shall declare at least one
    attribute of every type in ``hmd_meta_types.entity.type_mapping`` (string,
    integer, float, bool, enum, timestamp, epoch, collection, mapping, blob),
    and every one of its attributes shall be required.

.. req:: Every type, optional
    :id: HMD_LANG_CONFORMANCE_REQ_VOCAB_002
    :status: implemented

    The noun ``hmd_lang_conformance.typed_optional`` shall declare at least one
    attribute of every type in ``type_mapping``, and every attribute except
    ``label`` shall be optional, so the suites can test absent and removed
    values.

.. req:: A run label on every noun
    :id: HMD_LANG_CONFORMANCE_REQ_VOCAB_003
    :status: implemented

    Every noun shall declare a required ``string`` attribute ``label``, which
    the conformance suites set per run and search on, so they never depend on a
    clean database.

.. req:: Enums with several values
    :id: HMD_LANG_CONFORMANCE_REQ_VOCAB_004
    :status: implemented

    Every ``enum`` attribute shall declare at least two values in ``enum_def``,
    so a suite can change an enum value and test a value outside the set.

.. req:: A relationship between the nouns
    :id: HMD_LANG_CONFORMANCE_REQ_VOCAB_005
    :status: implemented

    The relationship ``hmd_lang_conformance.typed_optional_has_typed_required``
    shall run from ``typed_optional`` to ``typed_required``, so the suites can
    test relationships and deleted endpoints.
