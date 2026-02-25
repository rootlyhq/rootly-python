from typing import Literal, cast

NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers = Literal[
    "admins", "all", "escalate"
]

NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES: set[
    NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers
] = {
    "admins",
    "all",
    "escalate",
}


def check_new_escalation_policy_level_data_attributes_notification_target_params_item_type_0_team_members(
    value: str | None,
) -> NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES:
        return cast(NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0TeamMembers, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_LEVEL_DATA_ATTRIBUTES_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES!r}"
    )
