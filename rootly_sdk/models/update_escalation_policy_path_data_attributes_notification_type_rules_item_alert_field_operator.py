from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertFieldOperator = Literal[
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_empty",
    "is_not",
    "is_not_empty",
    "is_not_one_of",
    "is_one_of",
    "matches",
    "starts_with",
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_OPERATOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertFieldOperator
] = {
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_empty",
    "is_not",
    "is_not_empty",
    "is_not_one_of",
    "is_one_of",
    "matches",
    "starts_with",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field_operator(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertFieldOperator | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_OPERATOR_VALUES!r}"
    )
