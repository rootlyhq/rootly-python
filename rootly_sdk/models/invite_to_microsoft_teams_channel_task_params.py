from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_to_microsoft_teams_channel_task_params_task_type import (
    InviteToMicrosoftTeamsChannelTaskParamsTaskType,
    check_invite_to_microsoft_teams_channel_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invite_to_microsoft_teams_channel_task_params_channel import (
        InviteToMicrosoftTeamsChannelTaskParamsChannel,
    )
    from ..models.invite_to_microsoft_teams_channel_task_params_team import InviteToMicrosoftTeamsChannelTaskParamsTeam


T = TypeVar("T", bound="InviteToMicrosoftTeamsChannelTaskParams")


@_attrs_define
class InviteToMicrosoftTeamsChannelTaskParams:
    """
    Attributes:
        channel (InviteToMicrosoftTeamsChannelTaskParamsChannel):
        emails (str): Comma separated list of emails to invite
        task_type (Union[Unset, InviteToMicrosoftTeamsChannelTaskParamsTaskType]):
        team (Union[Unset, InviteToMicrosoftTeamsChannelTaskParamsTeam]):
    """

    channel: "InviteToMicrosoftTeamsChannelTaskParamsChannel"
    emails: str
    task_type: Unset | InviteToMicrosoftTeamsChannelTaskParamsTaskType = UNSET
    team: Union[Unset, "InviteToMicrosoftTeamsChannelTaskParamsTeam"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.to_dict()

        emails = self.emails

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        team: Unset | dict[str, Any] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "emails": emails,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_to_microsoft_teams_channel_task_params_channel import (
            InviteToMicrosoftTeamsChannelTaskParamsChannel,
        )
        from ..models.invite_to_microsoft_teams_channel_task_params_team import (
            InviteToMicrosoftTeamsChannelTaskParamsTeam,
        )

        d = dict(src_dict)
        channel = InviteToMicrosoftTeamsChannelTaskParamsChannel.from_dict(d.pop("channel"))

        emails = d.pop("emails")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | InviteToMicrosoftTeamsChannelTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_invite_to_microsoft_teams_channel_task_params_task_type(_task_type)

        _team = d.pop("team", UNSET)
        team: Unset | InviteToMicrosoftTeamsChannelTaskParamsTeam
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = InviteToMicrosoftTeamsChannelTaskParamsTeam.from_dict(_team)

        invite_to_microsoft_teams_channel_task_params = cls(
            channel=channel,
            emails=emails,
            task_type=task_type,
            team=team,
        )

        invite_to_microsoft_teams_channel_task_params.additional_properties = d
        return invite_to_microsoft_teams_channel_task_params

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
