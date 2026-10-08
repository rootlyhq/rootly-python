from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemNotificationType = Literal["audible", "quiet"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemNotificationType
] = {
    "audible",
    "quiet",
}


def check_escalation_policy_path_notification_type_rules_item_notification_type(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemNotificationType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
