from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rename_microsoft_teams_channel_task_params_task_type import (
    RenameMicrosoftTeamsChannelTaskParamsTaskType,
    check_rename_microsoft_teams_channel_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rename_microsoft_teams_channel_task_params_channel import RenameMicrosoftTeamsChannelTaskParamsChannel
    from ..models.rename_microsoft_teams_channel_task_params_team import RenameMicrosoftTeamsChannelTaskParamsTeam


T = TypeVar("T", bound="RenameMicrosoftTeamsChannelTaskParams")


@_attrs_define
class RenameMicrosoftTeamsChannelTaskParams:
    """
    Attributes:
        team (RenameMicrosoftTeamsChannelTaskParamsTeam):
        channel (RenameMicrosoftTeamsChannelTaskParamsChannel):
        title (str):
        task_type (Union[Unset, RenameMicrosoftTeamsChannelTaskParamsTaskType]):
    """

    team: "RenameMicrosoftTeamsChannelTaskParamsTeam"
    channel: "RenameMicrosoftTeamsChannelTaskParamsChannel"
    title: str
    task_type: Unset | RenameMicrosoftTeamsChannelTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team = self.team.to_dict()

        channel = self.channel.to_dict()

        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "channel": channel,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rename_microsoft_teams_channel_task_params_channel import (
            RenameMicrosoftTeamsChannelTaskParamsChannel,
        )
        from ..models.rename_microsoft_teams_channel_task_params_team import RenameMicrosoftTeamsChannelTaskParamsTeam

        d = dict(src_dict)
        team = RenameMicrosoftTeamsChannelTaskParamsTeam.from_dict(d.pop("team"))

        channel = RenameMicrosoftTeamsChannelTaskParamsChannel.from_dict(d.pop("channel"))

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | RenameMicrosoftTeamsChannelTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_rename_microsoft_teams_channel_task_params_task_type(_task_type)

        rename_microsoft_teams_channel_task_params = cls(
            team=team,
            channel=channel,
            title=title,
            task_type=task_type,
        )

        rename_microsoft_teams_channel_task_params.additional_properties = d
        return rename_microsoft_teams_channel_task_params

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
