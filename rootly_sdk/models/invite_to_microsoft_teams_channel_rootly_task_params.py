from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_to_microsoft_teams_channel_rootly_task_params_task_type import (
    InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType,
    check_invite_to_microsoft_teams_channel_rootly_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params_channel import (
        InviteToMicrosoftTeamsChannelRootlyTaskParamsChannel,
    )
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params_escalation_policy_target import (
        InviteToMicrosoftTeamsChannelRootlyTaskParamsEscalationPolicyTarget,
    )
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params_group_target import (
        InviteToMicrosoftTeamsChannelRootlyTaskParamsGroupTarget,
    )
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params_schedule_target import (
        InviteToMicrosoftTeamsChannelRootlyTaskParamsScheduleTarget,
    )
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params_service_target import (
        InviteToMicrosoftTeamsChannelRootlyTaskParamsServiceTarget,
    )
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params_team import (
        InviteToMicrosoftTeamsChannelRootlyTaskParamsTeam,
    )
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params_user_target import (
        InviteToMicrosoftTeamsChannelRootlyTaskParamsUserTarget,
    )


T = TypeVar("T", bound="InviteToMicrosoftTeamsChannelRootlyTaskParams")


@_attrs_define
class InviteToMicrosoftTeamsChannelRootlyTaskParams:
    """
    Attributes:
        team (InviteToMicrosoftTeamsChannelRootlyTaskParamsTeam):
        channel (InviteToMicrosoftTeamsChannelRootlyTaskParamsChannel):
        task_type (Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType]):
        escalation_policy_target (Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsEscalationPolicyTarget]):
        service_target (Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsServiceTarget]):
        user_target (Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsUserTarget]):
        group_target (Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsGroupTarget]):
        schedule_target (Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsScheduleTarget]):
    """

    team: "InviteToMicrosoftTeamsChannelRootlyTaskParamsTeam"
    channel: "InviteToMicrosoftTeamsChannelRootlyTaskParamsChannel"
    task_type: Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType] = UNSET
    escalation_policy_target: Union[Unset, "InviteToMicrosoftTeamsChannelRootlyTaskParamsEscalationPolicyTarget"] = (
        UNSET
    )
    service_target: Union[Unset, "InviteToMicrosoftTeamsChannelRootlyTaskParamsServiceTarget"] = UNSET
    user_target: Union[Unset, "InviteToMicrosoftTeamsChannelRootlyTaskParamsUserTarget"] = UNSET
    group_target: Union[Unset, "InviteToMicrosoftTeamsChannelRootlyTaskParamsGroupTarget"] = UNSET
    schedule_target: Union[Unset, "InviteToMicrosoftTeamsChannelRootlyTaskParamsScheduleTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team = self.team.to_dict()

        channel = self.channel.to_dict()

        task_type: Union[Unset, str] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        escalation_policy_target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.escalation_policy_target, Unset):
            escalation_policy_target = self.escalation_policy_target.to_dict()

        service_target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_target, Unset):
            service_target = self.service_target.to_dict()

        user_target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_target, Unset):
            user_target = self.user_target.to_dict()

        group_target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group_target, Unset):
            group_target = self.group_target.to_dict()

        schedule_target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule_target, Unset):
            schedule_target = self.schedule_target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team": team,
                "channel": channel,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if escalation_policy_target is not UNSET:
            field_dict["escalation_policy_target"] = escalation_policy_target
        if service_target is not UNSET:
            field_dict["service_target"] = service_target
        if user_target is not UNSET:
            field_dict["user_target"] = user_target
        if group_target is not UNSET:
            field_dict["group_target"] = group_target
        if schedule_target is not UNSET:
            field_dict["schedule_target"] = schedule_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params_channel import (
            InviteToMicrosoftTeamsChannelRootlyTaskParamsChannel,
        )
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params_escalation_policy_target import (
            InviteToMicrosoftTeamsChannelRootlyTaskParamsEscalationPolicyTarget,
        )
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params_group_target import (
            InviteToMicrosoftTeamsChannelRootlyTaskParamsGroupTarget,
        )
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params_schedule_target import (
            InviteToMicrosoftTeamsChannelRootlyTaskParamsScheduleTarget,
        )
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params_service_target import (
            InviteToMicrosoftTeamsChannelRootlyTaskParamsServiceTarget,
        )
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params_team import (
            InviteToMicrosoftTeamsChannelRootlyTaskParamsTeam,
        )
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params_user_target import (
            InviteToMicrosoftTeamsChannelRootlyTaskParamsUserTarget,
        )

        d = dict(src_dict)
        team = InviteToMicrosoftTeamsChannelRootlyTaskParamsTeam.from_dict(d.pop("team"))

        channel = InviteToMicrosoftTeamsChannelRootlyTaskParamsChannel.from_dict(d.pop("channel"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_invite_to_microsoft_teams_channel_rootly_task_params_task_type(_task_type)

        _escalation_policy_target = d.pop("escalation_policy_target", UNSET)
        escalation_policy_target: Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsEscalationPolicyTarget]
        if isinstance(_escalation_policy_target, Unset):
            escalation_policy_target = UNSET
        else:
            escalation_policy_target = InviteToMicrosoftTeamsChannelRootlyTaskParamsEscalationPolicyTarget.from_dict(
                _escalation_policy_target
            )

        _service_target = d.pop("service_target", UNSET)
        service_target: Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsServiceTarget]
        if isinstance(_service_target, Unset):
            service_target = UNSET
        else:
            service_target = InviteToMicrosoftTeamsChannelRootlyTaskParamsServiceTarget.from_dict(_service_target)

        _user_target = d.pop("user_target", UNSET)
        user_target: Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsUserTarget]
        if isinstance(_user_target, Unset):
            user_target = UNSET
        else:
            user_target = InviteToMicrosoftTeamsChannelRootlyTaskParamsUserTarget.from_dict(_user_target)

        _group_target = d.pop("group_target", UNSET)
        group_target: Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsGroupTarget]
        if isinstance(_group_target, Unset):
            group_target = UNSET
        else:
            group_target = InviteToMicrosoftTeamsChannelRootlyTaskParamsGroupTarget.from_dict(_group_target)

        _schedule_target = d.pop("schedule_target", UNSET)
        schedule_target: Union[Unset, InviteToMicrosoftTeamsChannelRootlyTaskParamsScheduleTarget]
        if isinstance(_schedule_target, Unset):
            schedule_target = UNSET
        else:
            schedule_target = InviteToMicrosoftTeamsChannelRootlyTaskParamsScheduleTarget.from_dict(_schedule_target)

        invite_to_microsoft_teams_channel_rootly_task_params = cls(
            team=team,
            channel=channel,
            task_type=task_type,
            escalation_policy_target=escalation_policy_target,
            service_target=service_target,
            user_target=user_target,
            group_target=group_target,
            schedule_target=schedule_target,
        )

        invite_to_microsoft_teams_channel_rootly_task_params.additional_properties = d
        return invite_to_microsoft_teams_channel_rootly_task_params

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
