from typing import Literal

EscalationPolicyPathNotificationTypeRulesItemJSONPathOperator = Literal[
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

ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_OPERATOR_VALUES: set[
    EscalationPolicyPathNotificationTypeRulesItemJSONPathOperator
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


def check_escalation_policy_path_notification_type_rules_item_json_path_operator(
    value: str | None,
) -> EscalationPolicyPathNotificationTypeRulesItemJSONPathOperator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_NOTIFICATION_TYPE_RULES_ITEM_JSON_PATH_OPERATOR_VALUES!r}"
    )
