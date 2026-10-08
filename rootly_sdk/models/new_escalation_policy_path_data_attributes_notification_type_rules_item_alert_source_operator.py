from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceOperator = Literal[
    "is", "is_not", "is_not_one_of", "is_one_of"
]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_OPERATOR_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceOperator
] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_operator(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceOperator | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_OPERATOR_VALUES!r}"
    )
