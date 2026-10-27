# The code in this file is generated automatically.
# DO NOT EDIT!
from hmd_graphql_client.hmd_base_client import BaseClient
from typing import List
from hmd_schema_loader.hmd_schema_loader import get_default_loader, get_schema_root


from .typed_optional import TypedOptional
from .typed_required import TypedRequired



from .typed_optional_has_typed_required import TypedOptionalHasTypedRequired

def get_client_loader():
    return get_default_loader("hmd_lang_conformance")

def get_client_schema_root():
    return get_schema_root("hmd_lang_conformance")

class HmdLangConformanceClient:
    def __init__(self, base_client: BaseClient):
        self._base_client = base_client

    # Generic upsert...
    def upsert(self, entity):
        return self._base_client.upsert_entity(entity)

    # Generic delete...
    def delete(self, entity):
        self._base_client.delete_entity(entity.get_namespace_name(), entity.identifier)

    # Nouns...

    # hmd_lang_conformance_typed_optional
    def get_typed_optional_hmd_lang_conformance(self, id_: str) -> TypedOptional:
        return self._base_client.get_entity(TypedOptional.get_namespace_name(), id_)

    def delete_typed_optional_hmd_lang_conformance(self, id_: str) -> None:
        self._base_client.delete_entity(TypedOptional.get_namespace_name(), id_)

    def upsert_typed_optional_hmd_lang_conformance(self, entity: TypedOptional) -> TypedOptional:
        if not isinstance(entity, TypedOptional):
            raise Exception("entity must be an instance of TypedOptional")
        return self._base_client.upsert_entity(entity)

    
    def search_typed_optional_hmd_lang_conformance(self, filter_: dict) -> List[TypedOptional]:
        return self._base_client.search_entity(TypedOptional.get_namespace_name(), filter_)

    # hmd_lang_conformance_typed_required
    def get_typed_required_hmd_lang_conformance(self, id_: str) -> TypedRequired:
        return self._base_client.get_entity(TypedRequired.get_namespace_name(), id_)

    def delete_typed_required_hmd_lang_conformance(self, id_: str) -> None:
        self._base_client.delete_entity(TypedRequired.get_namespace_name(), id_)

    def upsert_typed_required_hmd_lang_conformance(self, entity: TypedRequired) -> TypedRequired:
        if not isinstance(entity, TypedRequired):
            raise Exception("entity must be an instance of TypedRequired")
        return self._base_client.upsert_entity(entity)

    
    def search_typed_required_hmd_lang_conformance(self, filter_: dict) -> List[TypedRequired]:
        return self._base_client.search_entity(TypedRequired.get_namespace_name(), filter_)


    # Relationships...

    # hmd_lang_conformance_typed_optional_has_typed_required
    def delete_typed_optional_has_typed_required_hmd_lang_conformance(self, id_: str) -> None:
        self._base_client.delete_entity(TypedOptionalHasTypedRequired.get_namespace_name(), id_)

    def upsert_typed_optional_has_typed_required_hmd_lang_conformance(self, entity: TypedOptionalHasTypedRequired) -> TypedOptionalHasTypedRequired:
        if not isinstance(entity, TypedOptionalHasTypedRequired):
            raise Exception("entity must be an instance of TypedOptionalHasTypedRequired")
        return self._base_client.upsert_entity(entity)

    def get_from_typed_optional_has_typed_required_hmd_lang_conformance(self, entity: TypedOptional) -> List[TypedOptionalHasTypedRequired]:
        if not isinstance(entity, TypedOptional):
            raise Exception("entity must be an instance of TypedOptional")
        return self._base_client.get_relationships_from(entity, TypedOptionalHasTypedRequired.get_namespace_name())

    def get_to_typed_optional_has_typed_required_hmd_lang_conformance(self, entity: TypedRequired) -> List[TypedOptionalHasTypedRequired]:
        if not isinstance(entity, TypedRequired):
            raise Exception("entity must be an instance of TypedRequired")
        return self._base_client.get_relationships_to(entity, TypedOptionalHasTypedRequired.get_namespace_name())


