from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageComponentGroup")


@_attrs_define
class StatusPageComponentGroup:
    """
    Attributes:
        status_page_id (str):
        name (str): Name of the component group
        position (int): Position of the group on the status page's top-level list
        created_at (datetime.datetime): Date of creation
        updated_at (datetime.datetime): Date of last update
        description (None | str | Unset): Description of the component group
        collapsed_by_default (bool | Unset): Whether the group renders collapsed on the public page
    """

    status_page_id: str
    name: str
    position: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    collapsed_by_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page_id = self.status_page_id

        name = self.name

        position = self.position

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        collapsed_by_default = self.collapsed_by_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_page_id": status_page_id,
                "name": name,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if collapsed_by_default is not UNSET:
            field_dict["collapsed_by_default"] = collapsed_by_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_page_id = d.pop("status_page_id")

        name = d.pop("name")

        position = d.pop("position")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        collapsed_by_default = d.pop("collapsed_by_default", UNSET)

        status_page_component_group = cls(
            status_page_id=status_page_id,
            name=name,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            collapsed_by_default=collapsed_by_default,
        )

        status_page_component_group.additional_properties = d
        return status_page_component_group

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
