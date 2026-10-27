*** Settings ***
Documentation     Checks that the conformance vocabulary covers every hmd-meta-types
...               attribute type, required and optional, and that the generated
...               package matches its schemas. `make docker-test` runs this suite
...               in a Python container with the package installed. Each test names
...               the requirements it verifies; see docs/requirements/.
Library           Collections
Library           ${CURDIR}/VocabularyLib.py

*** Test Cases ***
Typed Required Covers Every Type, All Required
    [Tags]    REQ_VOCAB_001
    ${all}=         Meta Types Type Names
    ${required}=    Attribute Types    typed_required    required=${True}
    Lists Should Be Equal    ${required}    ${all}
    ${optional}=    Attribute Types    typed_required    required=${False}
    Should Be Empty    ${optional}

Typed Optional Covers Every Type, Optional Except Label
    [Tags]    REQ_VOCAB_002
    ${all}=      Meta Types Type Names
    ${types}=    Attribute Types    typed_optional
    Lists Should Be Equal    ${types}    ${all}
    Optional Attributes Except Label Are Optional    typed_optional

Every Noun Has A Required String Label
    [Tags]    REQ_VOCAB_003
    ${nouns}=    Nouns
    Should Not Be Empty    ${nouns}
    FOR    ${noun}    IN    @{nouns}
        ${schema}=    Schema    ${noun}
        Dictionary Should Contain Key    ${schema}[attributes]    label
        Should Be Equal    ${schema}[attributes][label][type]    string
        Should Be True    ${schema}[attributes][label][required]
    END

Every Enum Has Several Values
    [Tags]    REQ_VOCAB_004
    ${counts}=    Enum Value Counts
    Should Not Be Empty    ${counts}
    FOR    ${attr}    ${count}    IN    &{counts}
        Should Be True    ${count} >= 2    ${attr} has ${count} values
    END

The Relationship Runs From Optional To Required
    [Tags]    REQ_VOCAB_005
    ${rel}=    Schema    typed_optional_has_typed_required
    Should Be Equal    ${rel}[metatype]    relationship
    Should Be Equal    ${rel}[ref_from]    hmd_lang_conformance.typed_optional
    Should Be Equal    ${rel}[ref_to]    hmd_lang_conformance.typed_required

The Package Ships The Schemas Unchanged
    [Tags]    REQ_GEN_001
    ${diff}=    Packaged Schema Differences
    Should Be Empty    ${diff}    packaged schemas differ from src/schemas: ${diff}

Generated Classes Match Their Schemas
    [Tags]    REQ_GEN_002
    ${names}=    Schema Names
    FOR    ${name}    IN    @{names}
        ${schema}=       Schema    ${name}
        ${generated}=    Generated Definition    ${name}
        Should Be Equal    ${generated}    ${schema}
    END

The Client Module Exists For The Service Loader
    [Tags]    REQ_GEN_003
    ${exports}=    Client Module Exports
    Lists Should Be Equal    ${exports}    ${{["HmdLangConformanceClient", "get_client_loader"]}}

The Package Version Is meta-data VERSION
    [Tags]    REQ_PKG_001
    ${installed}=    Installed Version
    ${repo}=         Repo Version
    Should Be Equal    ${installed}    ${repo}
