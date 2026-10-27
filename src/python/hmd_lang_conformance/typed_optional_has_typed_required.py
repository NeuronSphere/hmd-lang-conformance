

from hmd_meta_types import Relationship, Noun, Entity
from hmd_lang_conformance.typed_optional import TypedOptional
from hmd_lang_conformance.typed_required import TypedRequired
from datetime import datetime
from typing import List, Dict, Any

class TypedOptionalHasTypedRequired(Relationship):

    _entity_def = \
        {'name': 'typed_optional_has_typed_required', 'namespace': 'hmd_lang_conformance', 'metatype': 'relationship', 'ref_from': 'hmd_lang_conformance.typed_optional', 'ref_to': 'hmd_lang_conformance.typed_required', 'attributes': {}, 'adornments': {'ref_from': {'arrow': False, 'cardinality': '1'}, 'ref_to': {'arrow': True, 'cardinality': '*'}}}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def entity_definition():
        return TypedOptionalHasTypedRequired._entity_def

    @staticmethod
    def get_namespace_name():
        return Entity.get_namespace_name(TypedOptionalHasTypedRequired._entity_def)


    @staticmethod
    def ref_from_type():
        return TypedOptional

    @staticmethod
    def ref_to_type():
        return TypedRequired

    

    