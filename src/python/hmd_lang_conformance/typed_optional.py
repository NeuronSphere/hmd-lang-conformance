

from hmd_meta_types import Relationship, Noun, Entity

from datetime import datetime
from typing import List, Dict, Any

class TypedOptional(Noun):

    _entity_def = \
        {'name': 'typed_optional', 'namespace': 'hmd_lang_conformance', 'metatype': 'noun', 'description': 'Conformance noun with every attribute type optional (hmd-entity-storage NERD005 SPEC004).', 'attributes': {'label': {'type': 'string', 'description': 'Run-scoped label the suites search on.', 'required': True}, 's_string': {'type': 'string', 'description': 'A string attribute.', 'required': False}, 'i_integer': {'type': 'integer', 'description': 'A integer attribute.', 'required': False}, 'f_float': {'type': 'float', 'description': 'A float attribute.', 'required': False}, 'b_bool': {'type': 'bool', 'description': 'A bool attribute.', 'required': False}, 'e_enum': {'type': 'enum', 'description': 'A enum attribute.', 'required': False, 'enum_def': ['RED', 'GREEN', 'BLUE']}, 'ts_timestamp': {'type': 'timestamp', 'description': 'A timestamp attribute.', 'required': False}, 'ep_epoch': {'type': 'epoch', 'description': 'A epoch attribute.', 'required': False}, 'c_collection': {'type': 'collection', 'description': 'A collection attribute.', 'required': False}, 'm_mapping': {'type': 'mapping', 'description': 'A mapping attribute.', 'required': False}, 'bl_blob': {'type': 'blob', 'description': 'A blob attribute.', 'required': False}}}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def entity_definition():
        return TypedOptional._entity_def

    @staticmethod
    def get_namespace_name():
        return Entity.get_namespace_name(TypedOptional._entity_def)


    

    
        
    @property
    def label(self) -> str:
        return self._getter("label")

    @label.setter
    def label(self, value: str) -> None:
        self._setter("label", value)
    
        
    @property
    def s_string(self) -> str:
        return self._getter("s_string")

    @s_string.setter
    def s_string(self, value: str) -> None:
        self._setter("s_string", value)
    
        
    @property
    def i_integer(self) -> int:
        return self._getter("i_integer")

    @i_integer.setter
    def i_integer(self, value: int) -> None:
        self._setter("i_integer", value)
    
        
    @property
    def f_float(self) -> float:
        return self._getter("f_float")

    @f_float.setter
    def f_float(self, value: float) -> None:
        self._setter("f_float", value)
    
        
    @property
    def b_bool(self) -> Any:
        return self._getter("b_bool")

    @b_bool.setter
    def b_bool(self, value: Any) -> None:
        self._setter("b_bool", value)
    
        
    @property
    def e_enum(self) -> str:
        return self._getter("e_enum")

    @e_enum.setter
    def e_enum(self, value: str) -> None:
        self._setter("e_enum", value)
    
        
    @property
    def ts_timestamp(self) -> datetime:
        return self._getter("ts_timestamp")

    @ts_timestamp.setter
    def ts_timestamp(self, value: datetime) -> None:
        self._setter("ts_timestamp", value)
    
        
    @property
    def ep_epoch(self) -> Any:
        return self._getter("ep_epoch")

    @ep_epoch.setter
    def ep_epoch(self, value: Any) -> None:
        self._setter("ep_epoch", value)
    
        
    @property
    def c_collection(self) -> List:
        return self._getter("c_collection")

    @c_collection.setter
    def c_collection(self, value: List) -> None:
        self._setter("c_collection", value)
    
        
    @property
    def m_mapping(self) -> Dict:
        return self._getter("m_mapping")

    @m_mapping.setter
    def m_mapping(self, value: Dict) -> None:
        self._setter("m_mapping", value)
    
        
    @property
    def bl_blob(self) -> bytes:
        return self._getter("bl_blob")

    @bl_blob.setter
    def bl_blob(self, value: bytes) -> None:
        self._setter("bl_blob", value)
    

    
    
    
        
    def get_from_typed_optional_has_typed_required_hmd_lang_conformance(self):
        return self.from_rels["hmd_lang_conformance.typed_optional_has_typed_required"]
    
    