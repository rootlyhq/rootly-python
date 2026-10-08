from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgencyOperator = Literal[
    "is", "is_not", "is_not_one_of", "is_one_of"
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_OPERATOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgencyOperator
] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency_operator(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgencyOperator | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_OPERATOR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_URGENCY_OPERATOR_VALUES!r}"
    )
