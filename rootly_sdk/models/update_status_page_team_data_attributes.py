from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_status_page_team_data_attributes_permission_level import (
    UpdateStatusPageTeamDataAttributesPermissionLevel,
    check_update_status_page_team_data_attributes_permission_level,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusPageTeamDataAttributes")


@_attrs_define
class UpdateStatusPageTeamDataAttributes:
    """
    Attributes:
        permission_level (UpdateStatusPageTeamDataAttributesPermissionLevel | Unset): publish_only lets team members
            post status page updates and announcements. edit_and_publish also lets them edit the page, its components,
            templates, and subscribers
    """

    permission_level: UpdateStatusPageTeamDataAttributesPermissionLevel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        permission_level: str | Unset = UNSET
        if not isinstance(self.permission_level, Unset):
            permission_level = self.permission_level

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if permission_level is not UNSET:
            field_dict["permission_level"] = permission_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _permission_level = d.pop("permission_level", UNSET)
        permission_level: UpdateStatusPageTeamDataAttributesPermissionLevel | Unset
        if isinstance(_permission_level, Unset):
            permission_level = UNSET
        else:
            permission_level = check_update_status_page_team_data_attributes_permission_level(_permission_level)

        update_status_page_team_data_attributes = cls(
            permission_level=permission_level,
        )

        return update_status_page_team_data_attributes
