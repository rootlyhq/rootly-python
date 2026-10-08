from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_escalation_policy_level_data_attributes_notification_target_params_item_type_0_team_members import (
    UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers,
    check_update_escalation_policy_level_data_attributes_notification_target_params_item_type_0_team_members,
)
from ..models.update_escalation_policy_level_data_attributes_notification_target_params_item_type_0_type import (
    UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type,
    check_update_escalation_policy_level_data_attributes_notification_target_params_item_type_0_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0")


@_attrs_define
class UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0:
    """
    Attributes:
        id (str): The ID of notification target
        type_ (UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type): The type of the
            notification target
        team_members (UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers | Unset):
            For targets with type=team, controls whether to notify admins, all team members, or escalate to team EP.
    """

    id: str
    type_: UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0Type
    team_members: UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        team_members: str | Unset = UNSET
        if not isinstance(self.team_members, Unset):
            team_members = self.team_members

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if team_members is not UNSET:
            field_dict["team_members"] = team_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_update_escalation_policy_level_data_attributes_notification_target_params_item_type_0_type(
            d.pop("type")
        )

        _team_members = d.pop("team_members", UNSET)
        team_members: UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers | Unset
        if isinstance(_team_members, Unset):
            team_members = UNSET
        else:
            team_members = check_update_escalation_policy_level_data_attributes_notification_target_params_item_type_0_team_members(
                _team_members
            )

        update_escalation_policy_level_data_attributes_notification_target_params_item_type_0 = cls(
            id=id,
            type_=type_,
            team_members=team_members,
        )

        return update_escalation_policy_level_data_attributes_notification_target_params_item_type_0
