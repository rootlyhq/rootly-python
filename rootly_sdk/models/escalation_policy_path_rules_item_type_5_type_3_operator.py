from typing import Literal, cast

EscalationPolicyPathRulesItemType5Type3Operator = Literal[
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

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_TYPE_3_OPERATOR_VALUES: set[
    EscalationPolicyPathRulesItemType5Type3Operator
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


def check_escalation_policy_path_rules_item_type_5_type_3_operator(
    value: str | None,
) -> EscalationPolicyPathRulesItemType5Type3Operator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_TYPE_3_OPERATOR_VALUES:
        return cast(EscalationPolicyPathRulesItemType5Type3Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_TYPE_3_OPERATOR_VALUES!r}"
    )
