from typing import Literal, cast

EscalationPolicyLevelNotificationTargetParamsItemType0TeamMembers = Literal["admins", "all", "escalate"]

ESCALATION_POLICY_LEVEL_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES: set[
    EscalationPolicyLevelNotificationTargetParamsItemType0TeamMembers
] = {
    "admins",
    "all",
    "escalate",
}


def check_escalation_policy_level_notification_target_params_item_type_0_team_members(
    value: str | None,
) -> EscalationPolicyLevelNotificationTargetParamsItemType0TeamMembers | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LEVEL_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES:
        return cast(EscalationPolicyLevelNotificationTargetParamsItemType0TeamMembers, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LEVEL_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TEAM_MEMBERS_VALUES!r}"
    )
