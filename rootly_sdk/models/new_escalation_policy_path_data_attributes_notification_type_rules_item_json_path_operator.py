from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathOperator = Literal[
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_not",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches",
    "starts_with",
]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_OPERATOR_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathOperator
] = {
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_not",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches",
    "starts_with",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_json_path_operator(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPathOperator | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_OPERATOR_VALUES!r}"
    )
