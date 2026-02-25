from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_entity_property_key import CatalogEntityPropertyKey, check_catalog_entity_property_key

T = TypeVar("T", bound="CatalogEntityProperty")


@_attrs_define
class CatalogEntityProperty:
    """**Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or native catalog
    endpoints (teams, services, functionalities, incident_types, causes, environments) to retrieve field values instead.

        Attributes:
            catalog_entity_id (str):
            catalog_field_id (str):
            key (CatalogEntityPropertyKey):
            value (str):
            created_at (str):
            updated_at (str):
    """

    catalog_entity_id: str
    catalog_field_id: str
    key: CatalogEntityPropertyKey
    value: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_entity_id = self.catalog_entity_id

        catalog_field_id = self.catalog_field_id

        key: str = self.key

        value = self.value

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_entity_id": catalog_entity_id,
                "catalog_field_id": catalog_field_id,
                "key": key,
                "value": value,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog_entity_id = d.pop("catalog_entity_id")

        catalog_field_id = d.pop("catalog_field_id")

        key = check_catalog_entity_property_key(d.pop("key"))

        value = d.pop("value")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        catalog_entity_property = cls(
            catalog_entity_id=catalog_entity_id,
            catalog_field_id=catalog_field_id,
            key=key,
            value=value,
            created_at=created_at,
            updated_at=updated_at,
        )

        catalog_entity_property.additional_properties = d
        return catalog_entity_property

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
