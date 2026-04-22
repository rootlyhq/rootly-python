from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entity_properties_item import CatalogEntityPropertiesItem


T = TypeVar("T", bound="CatalogEntity")


@_attrs_define
class CatalogEntity:
    """
    Attributes:
        name (str):
        position (int | None): Default position of the item when displayed in a list.
        created_at (str):
        updated_at (str):
        description (None | str | Unset):
        properties (list[CatalogEntityPropertiesItem] | Unset): Array of property values for this catalog entity
    """

    name: str
    position: int | None
    created_at: str
    updated_at: str
    description: None | str | Unset = UNSET
    properties: list[CatalogEntityPropertiesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        position: int | None
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_entity_properties_item import CatalogEntityPropertiesItem

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_position(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: list[CatalogEntityPropertiesItem] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = CatalogEntityPropertiesItem.from_dict(properties_item_data)

                properties.append(properties_item)

        catalog_entity = cls(
            name=name,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            properties=properties,
        )

        catalog_entity.additional_properties = d
        return catalog_entity

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
