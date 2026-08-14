from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusPageComponentGroupDataAttributes")


@_attrs_define
class UpdateStatusPageComponentGroupDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): Name of the component group
        description (Union[None, Unset, str]): Description of the component group
        position (Union[Unset, int]): Position of the group on the status page's top-level list (shared with ungrouped
            components)
        collapsed_by_default (Union[None, Unset, bool]): Whether the group renders collapsed on the public page
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    position: Unset | int = UNSET
    collapsed_by_default: None | Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position = self.position

        collapsed_by_default: None | Unset | bool
        if isinstance(self.collapsed_by_default, Unset):
            collapsed_by_default = UNSET
        else:
            collapsed_by_default = self.collapsed_by_default

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if collapsed_by_default is not UNSET:
            field_dict["collapsed_by_default"] = collapsed_by_default

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

        position = d.pop("position", UNSET)

        def _parse_collapsed_by_default(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        collapsed_by_default = _parse_collapsed_by_default(d.pop("collapsed_by_default", UNSET))

        update_status_page_component_group_data_attributes = cls(
            name=name,
            description=description,
            position=position,
            collapsed_by_default=collapsed_by_default,
        )

        return update_status_page_component_group_data_attributes
