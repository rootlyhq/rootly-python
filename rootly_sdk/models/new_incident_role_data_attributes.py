from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentRoleDataAttributes")


@_attrs_define
class NewIncidentRoleDataAttributes:
    """
    Attributes:
        name (str): The name of the incident role
        summary (Union[None, Unset, str]): The summary of the incident role
        description (Union[None, Unset, str]): The description of the incident role
        position (Union[None, Unset, int]): Position of the incident role
        optional (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        allow_multi_user_assignment (Union[Unset, bool]):
    """

    name: str
    summary: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    optional: Unset | bool = UNSET
    enabled: Unset | bool = UNSET
    allow_multi_user_assignment: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        summary: None | Unset | str
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        optional = self.optional

        enabled = self.enabled

        allow_multi_user_assignment = self.allow_multi_user_assignment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if optional is not UNSET:
            field_dict["optional"] = optional
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if allow_multi_user_assignment is not UNSET:
            field_dict["allow_multi_user_assignment"] = allow_multi_user_assignment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_summary(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        optional = d.pop("optional", UNSET)

        enabled = d.pop("enabled", UNSET)

        allow_multi_user_assignment = d.pop("allow_multi_user_assignment", UNSET)

        new_incident_role_data_attributes = cls(
            name=name,
            summary=summary,
            description=description,
            position=position,
            optional=optional,
            enabled=enabled,
            allow_multi_user_assignment=allow_multi_user_assignment,
        )

        return new_incident_role_data_attributes
