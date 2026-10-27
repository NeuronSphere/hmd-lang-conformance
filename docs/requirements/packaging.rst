Packaging
=========

.. req:: The package version is meta-data/VERSION
    :id: HMD_LANG_CONFORMANCE_REQ_PKG_001
    :status: implemented

    The installed distribution ``hmd-lang-conformance`` shall report the version
    in ``meta-data/VERSION``.

.. req:: A conformance service image
    :id: HMD_LANG_CONFORMANCE_REQ_PKG_002
    :status: implemented
    :tags: trace-exempt

    ``make conformance-image`` shall build the published ``hmd-ms-base-test``
    image with this package installed, tagged ``hmd-ms-base-test:0.1`` for a
    local nsctl deploy.

    **Verified by** ``hmd-entity-storage``'s conformance suites
    (``test/01_crud.robot`` to ``test/09_bulk_upsert.robot``) run against that
    image with ``hmd-bender --label python-<engine>``; no test in this repo can
    deploy a service.

    Known issue: :need:`HMD_LANG_CONFORMANCE_ISSUE_004`.
