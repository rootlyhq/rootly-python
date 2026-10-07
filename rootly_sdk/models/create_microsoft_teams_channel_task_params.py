from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_microsoft_teams_channel_task_params_private import (
    CreateMicrosoftTeamsChannelTaskParamsPrivate,
    check_create_microsoft_teams_channel_task_params_private,
)
from ..models.create_microsoft_teams_channel_task_params_task_type import (
    CreateMicrosoftTeamsChannelTaskParamsTaskType,
    check_create_microsoft_teams_channel_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_microsoft_teams_channel_task_params_team import CreateMicrosoftTeamsChannelTaskParamsTeam


T = TypeVar("T", bound="CreateMicrosoftTeamsChannelTaskParams")


@_attrs_define
class CreateMicrosoftTeamsChannelTaskParams:
    """
    Attributes:
        team (CreateMicrosoftTeamsChannelTaskParamsTeam):
        title (str): Microsoft Team channel title
        task_type (CreateMicrosoftTeamsChannelTaskParamsTaskType | Unset):
        description (str | Unset): Microsoft Team channel description
        private (CreateMicrosoftTeamsChannelTaskParamsPrivate | Unset):  Default: 'auto'.
    """

    team: CreateMicrosoftTeamsChannelTaskParamsTeam
    title: str
    task_type: CreateMicrosoftTeamsChannelTaskParamsTaskType | Unset = UNSET
    description: str | Unset = UNSET
    private: CreateMicrosoftTeamsChannelTaskParamsPrivate | Unset = "auto"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team = self.team.to_dict()

        title = self.title

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        private: str | Unset = UNSET
        if not isinstance(self.private, Unset):
            private = self.private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_microsoft_teams_channel_task_params_team import CreateMicrosoftTeamsChannelTaskParamsTeam

        d = dict(src_dict)
        team = CreateMicrosoftTeamsChannelTaskParamsTeam.from_dict(d.pop("team"))

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateMicrosoftTeamsChannelTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_microsoft_teams_channel_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        _private = d.pop("private", UNSET)
        private: CreateMicrosoftTeamsChannelTaskParamsPrivate | Unset
        if isinstance(_private, Unset):
            private = UNSET
        else:
            private = check_create_microsoft_teams_channel_task_params_private(_private)

        create_microsoft_teams_channel_task_params = cls(
            team=team,
            title=title,
            task_type=task_type,
            description=description,
            private=private,
        )

        create_microsoft_teams_channel_task_params.additional_properties = d
        return create_microsoft_teams_channel_task_params

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
