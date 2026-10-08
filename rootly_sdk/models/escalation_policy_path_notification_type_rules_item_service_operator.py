from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemServiceOperator = Literal["is", "is_not", "is_not_one_of", "is_one_of"]

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_SERVICE_OPERATOR_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemServiceOperator
] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_policy_path_notification_type_rules_item_service_operator(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemServiceOperator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_SERVICE_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_SERVICE_OPERATOR_VALUES!r}"
    )
