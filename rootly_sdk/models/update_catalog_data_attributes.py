from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_catalog_data_attributes_icon import (
    UpdateCatalogDataAttributesIcon,
    check_update_catalog_data_attributes_icon,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCatalogDataAttributes")


@_attrs_define
class UpdateCatalogDataAttributes:
    """
    Attributes:
        name (str | Unset):
        description (None | str | Unset):
        icon (UpdateCatalogDataAttributesIcon | Unset):
        position (int | None | Unset): Default position of the catalog when displayed in a list.
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    icon: UpdateCatalogDataAttributesIcon | Unset = UNSET
    position: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon: str | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _icon = d.pop("icon", UNSET)
        icon: UpdateCatalogDataAttributesIcon | Unset
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = check_update_catalog_data_attributes_icon(_icon)

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        update_catalog_data_attributes = cls(
            name=name,
            description=description,
            icon=icon,
            position=position,
        )

        return update_catalog_data_attributes
