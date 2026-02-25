from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

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
        title (str): Microsoft Team channel title
        task_type (Union[Unset, CreateMicrosoftTeamsChannelTaskParamsTaskType]):
        team (Union[Unset, CreateMicrosoftTeamsChannelTaskParamsTeam]):
        description (Union[Unset, str]): Microsoft Team channel description
        private (Union[Unset, CreateMicrosoftTeamsChannelTaskParamsPrivate]):  Default: 'auto'.
    """

    title: str
    task_type: Unset | CreateMicrosoftTeamsChannelTaskParamsTaskType = UNSET
    team: Union[Unset, "CreateMicrosoftTeamsChannelTaskParamsTeam"] = UNSET
    description: Unset | str = UNSET
    private: Unset | CreateMicrosoftTeamsChannelTaskParamsPrivate = "auto"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        team: Unset | dict[str, Any] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        description = self.description

        private: Unset | str = UNSET
        if not isinstance(self.private, Unset):
            private = self.private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if team is not UNSET:
            field_dict["team"] = team
        if description is not UNSET:
            field_dict["description"] = description
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_microsoft_teams_channel_task_params_team import CreateMicrosoftTeamsChannelTaskParamsTeam

        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateMicrosoftTeamsChannelTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_microsoft_teams_channel_task_params_task_type(_task_type)

        _team = d.pop("team", UNSET)
        team: Unset | CreateMicrosoftTeamsChannelTaskParamsTeam
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = CreateMicrosoftTeamsChannelTaskParamsTeam.from_dict(_team)

        description = d.pop("description", UNSET)

        _private = d.pop("private", UNSET)
        private: Unset | CreateMicrosoftTeamsChannelTaskParamsPrivate
        if isinstance(_private, Unset):
            private = UNSET
        else:
            private = check_create_microsoft_teams_channel_task_params_private(_private)

        create_microsoft_teams_channel_task_params = cls(
            title=title,
            task_type=task_type,
            team=team,
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
