from typing import Literal, cast

EscalationPolicyPathRulesItemType6Type2Operator = Literal[
    "contains", "does_not_contain", "is", "is_not", "is_not_one_of", "is_one_of"
]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_2_OPERATOR_VALUES: set[
    EscalationPolicyPathRulesItemType6Type2Operator
] = {
    "contains",
    "does_not_contain",
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_policy_path_rules_item_type_6_type_2_operator(
    value: str | None,
) -> EscalationPolicyPathRulesItemType6Type2Operator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_2_OPERATOR_VALUES:
        return cast(EscalationPolicyPathRulesItemType6Type2Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_2_OPERATOR_VALUES!r}"
    )
