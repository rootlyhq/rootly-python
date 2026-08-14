from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_catalog_entity_property_data_attributes_key import (
    NewCatalogEntityPropertyDataAttributesKey,
    check_new_catalog_entity_property_data_attributes_key,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCatalogEntityPropertyDataAttributes")


@_attrs_define
class NewCatalogEntityPropertyDataAttributes:
    """Maximum of 50 values allowed per catalog field.

    Attributes:
        catalog_field_id (str):
        key (NewCatalogEntityPropertyDataAttributesKey):
        value (str):
        catalog_entity_id (Union[Unset, str]):
    """

    catalog_field_id: str
    key: NewCatalogEntityPropertyDataAttributesKey
    value: str
    catalog_entity_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        catalog_field_id = self.catalog_field_id

        key: str = self.key

        value = self.value

        catalog_entity_id = self.catalog_entity_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "catalog_field_id": catalog_field_id,
                "key": key,
                "value": value,
            }
        )
        if catalog_entity_id is not UNSET:
            field_dict["catalog_entity_id"] = catalog_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog_field_id = d.pop("catalog_field_id")

        key = check_new_catalog_entity_property_data_attributes_key(d.pop("key"))

        value = d.pop("value")

        catalog_entity_id = d.pop("catalog_entity_id", UNSET)

        new_catalog_entity_property_data_attributes = cls(
            catalog_field_id=catalog_field_id,
            key=key,
            value=value,
            catalog_entity_id=catalog_entity_id,
        )

        return new_catalog_entity_property_data_attributes
