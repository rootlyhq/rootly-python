from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentRoleDataAttributes")


@_attrs_define
class UpdateIncidentRoleDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the incident role
        summary (None | str | Unset): The summary of the incident role
        description (None | str | Unset): The description of the incident role
        position (int | None | Unset): Position of the incident role
        optional (bool | Unset):
        enabled (bool | Unset):
        allow_multi_user_assignment (bool | Unset):
    """

    name: str | Unset = UNSET
    summary: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    optional: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    allow_multi_user_assignment: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        optional = self.optional

        enabled = self.enabled

        allow_multi_user_assignment = self.allow_multi_user_assignment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        name = d.pop("name", UNSET)

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        optional = d.pop("optional", UNSET)

        enabled = d.pop("enabled", UNSET)

        allow_multi_user_assignment = d.pop("allow_multi_user_assignment", UNSET)

        update_incident_role_data_attributes = cls(
            name=name,
            summary=summary,
            description=description,
            position=position,
            optional=optional,
            enabled=enabled,
            allow_multi_user_assignment=allow_multi_user_assignment,
        )

        return update_incident_role_data_attributes
