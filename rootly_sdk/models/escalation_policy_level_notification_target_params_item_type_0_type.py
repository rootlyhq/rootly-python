from typing import Literal, cast

EscalationPolicyLevelNotificationTargetParamsItemType0Type = Literal[
    "schedule", "service", "slack_channel", "team", "user"
]

ESCALATION_POLICY_LEVEL_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TYPE_VALUES: set[
    EscalationPolicyLevelNotificationTargetParamsItemType0Type
] = {
    "schedule",
    "service",
    "slack_channel",
    "team",
    "user",
}


def check_escalation_policy_level_notification_target_params_item_type_0_type(
    value: str | None,
) -> EscalationPolicyLevelNotificationTargetParamsItemType0Type | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_LEVEL_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TYPE_VALUES:
        return cast(EscalationPolicyLevelNotificationTargetParamsItemType0Type, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_LEVEL_NOTIFICATION_TARGET_PARAMS_ITEM_TYPE_0_TYPE_VALUES!r}"
    )
