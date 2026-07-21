from typing import Literal, cast

EscalationPolicyPathRulesItemType8Type2Operator = Literal[
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

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_8_TYPE_2_OPERATOR_VALUES: set[
    EscalationPolicyPathRulesItemType8Type2Operator
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


def check_escalation_policy_path_rules_item_type_8_type_2_operator(
    value: str | None,
) -> EscalationPolicyPathRulesItemType8Type2Operator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_8_TYPE_2_OPERATOR_VALUES:
        return cast(EscalationPolicyPathRulesItemType8Type2Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_8_TYPE_2_OPERATOR_VALUES!r}"
    )
