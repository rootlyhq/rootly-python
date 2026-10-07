from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_team_permission_level import (
    StatusPageTeamPermissionLevel,
    check_status_page_team_permission_level,
)

T = TypeVar("T", bound="StatusPageTeam")


@_attrs_define
class StatusPageTeam:
    """
    Attributes:
        status_page_id (str): ID of the status page the team is assigned to
        group_id (UUID): ID of the team granted access to the status page
        permission_level (StatusPageTeamPermissionLevel): Access level granted to members of the team
        created_at (datetime.datetime): Date of creation
        updated_at (datetime.datetime): Date of last update
    """

    status_page_id: str
    group_id: UUID
    permission_level: StatusPageTeamPermissionLevel
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page_id = self.status_page_id

        group_id = str(self.group_id)

        permission_level: str = self.permission_level

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_page_id": status_page_id,
                "group_id": group_id,
                "permission_level": permission_level,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_page_id = d.pop("status_page_id")

        group_id = UUID(d.pop("group_id"))

        permission_level = check_status_page_team_permission_level(d.pop("permission_level"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        status_page_team = cls(
            status_page_id=status_page_id,
            group_id=group_id,
            permission_level=permission_level,
            created_at=created_at,
            updated_at=updated_at,
        )

        status_page_team.additional_properties = d
        return status_page_team

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
