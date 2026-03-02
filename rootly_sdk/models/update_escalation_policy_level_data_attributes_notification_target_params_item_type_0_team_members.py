from typing import Literal, cast

UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers = Literal[
    "admins", "all", "escalate"
]

UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES: set[
    UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers
] = {
    "admins",
    "all",
    "escalate",
}


def check_update_escalation_policy_level_data_attributes_notification_target_params_item_type_0_team_members(
    value: str | None,
) -> UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES
    ):
        return cast(UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES!r}"
    )
