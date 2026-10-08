from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.new_status_page_team_data_attributes_permission_level import (
    NewStatusPageTeamDataAttributesPermissionLevel,
    check_new_status_page_team_data_attributes_permission_level,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewStatusPageTeamDataAttributes")


@_attrs_define
class NewStatusPageTeamDataAttributes:
    """
    Attributes:
        group_id (UUID): ID of the team granted access to the status page. Teams are listed by GET /v1/teams. A status
            page accepts at most 50 teams
        permission_level (NewStatusPageTeamDataAttributesPermissionLevel | Unset): publish_only lets team members post
            status page updates and announcements. edit_and_publish also lets them edit the page, its components, templates,
            and subscribers. Defaults to edit_and_publish
    """

    group_id: UUID
    permission_level: NewStatusPageTeamDataAttributesPermissionLevel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = str(self.group_id)

        permission_level: str | Unset = UNSET
        if not isinstance(self.permission_level, Unset):
            permission_level = self.permission_level

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "group_id": group_id,
            }
        )
        if permission_level is not UNSET:
            field_dict["permission_level"] = permission_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = UUID(d.pop("group_id"))

        _permission_level = d.pop("permission_level", UNSET)
        permission_level: NewStatusPageTeamDataAttributesPermissionLevel | Unset
        if isinstance(_permission_level, Unset):
            permission_level = UNSET
        else:
            permission_level = check_new_status_page_team_data_attributes_permission_level(_permission_level)

        new_status_page_team_data_attributes = cls(
            group_id=group_id,
            permission_level=permission_level,
        )

        return new_status_page_team_data_attributes
