from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusPageComponentDataAttributes")


@_attrs_define
class UpdateStatusPageComponentDataAttributes:
    """
    Attributes:
        name (Union[None, Unset, str]): Name of the component (ad-hoc components only)
        description (Union[None, Unset, str]): Description of the component (ad-hoc components only)
        status_page_component_group_id (Union[None, Unset, str]): ID of the component group on the same status page
            (null moves the component to the top level)
        position (Union[Unset, int]): Position of the component (within its group, or on the page's top-level list when
            ungrouped)
    """

    name: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    status_page_component_group_id: None | Unset | str = UNSET
    position: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status_page_component_group_id: None | Unset | str
        if isinstance(self.status_page_component_group_id, Unset):
            status_page_component_group_id = UNSET
        else:
            status_page_component_group_id = self.status_page_component_group_id

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status_page_component_group_id is not UNSET:
            field_dict["status_page_component_group_id"] = status_page_component_group_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status_page_component_group_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        status_page_component_group_id = _parse_status_page_component_group_id(
            d.pop("status_page_component_group_id", UNSET)
        )

        position = d.pop("position", UNSET)

        update_status_page_component_data_attributes = cls(
            name=name,
            description=description,
            status_page_component_group_id=status_page_component_group_id,
            position=position,
        )

        return update_status_page_component_data_attributes
