from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateEnvironmentDataAttributesFieldsItem")


@_attrs_define
class UpdateEnvironmentDataAttributesFieldsItem:
    """Set a value for a catalog field

    Attributes:
        catalog_field_id (str): Catalog field ID
        value (str): The field value
    """

    catalog_field_id: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_field_id = self.catalog_field_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_field_id": catalog_field_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog_field_id = d.pop("catalog_field_id")

        value = d.pop("value")

        update_environment_data_attributes_fields_item = cls(
            catalog_field_id=catalog_field_id,
            value=value,
        )

        update_environment_data_attributes_fields_item.additional_properties = d
        return update_environment_data_attributes_fields_item

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
