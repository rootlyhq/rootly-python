from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentTypePropertiesItem")


@_attrs_define
class IncidentTypePropertiesItem:
    """Set a value for a catalog property

    Attributes:
        catalog_property_id (str): Catalog property ID
        value (str): The property value
    """

    catalog_property_id: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_property_id = self.catalog_property_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_property_id": catalog_property_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog_property_id = d.pop("catalog_property_id")

        value = d.pop("value")

        incident_type_properties_item = cls(
            catalog_property_id=catalog_property_id,
            value=value,
        )

        incident_type_properties_item.additional_properties = d
        return incident_type_properties_item

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
