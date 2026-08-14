from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_catalog_entity_property_data_attributes_key import (
    UpdateCatalogEntityPropertyDataAttributesKey,
    check_update_catalog_entity_property_data_attributes_key,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCatalogEntityPropertyDataAttributes")


@_attrs_define
class UpdateCatalogEntityPropertyDataAttributes:
    """
    Attributes:
        key (Union[Unset, UpdateCatalogEntityPropertyDataAttributesKey]):
        value (Union[Unset, str]):
    """

    key: Unset | UpdateCatalogEntityPropertyDataAttributesKey = UNSET
    value: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        key: Unset | str = UNSET
        if not isinstance(self.key, Unset):
            key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: Unset | UpdateCatalogEntityPropertyDataAttributesKey
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = check_update_catalog_entity_property_data_attributes_key(_key)

        value = d.pop("value", UNSET)

        update_catalog_entity_property_data_attributes = cls(
            key=key,
            value=value,
        )

        return update_catalog_entity_property_data_attributes
