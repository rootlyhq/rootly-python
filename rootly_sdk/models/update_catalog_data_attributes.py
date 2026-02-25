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
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        icon (Union[Unset, UpdateCatalogDataAttributesIcon]):
        position (Union[None, Unset, int]): Default position of the catalog when displayed in a list.
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    icon: Unset | UpdateCatalogDataAttributesIcon = UNSET
    position: None | Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon: Unset | str = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        position: None | Unset | int
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

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _icon = d.pop("icon", UNSET)
        icon: Unset | UpdateCatalogDataAttributesIcon
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = check_update_catalog_data_attributes_icon(_icon)

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        update_catalog_data_attributes = cls(
            name=name,
            description=description,
            icon=icon,
            position=position,
        )

        return update_catalog_data_attributes
