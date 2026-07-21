from typing import Literal, cast

EscalationPolicyPathRulesItemType9Type6Operator = Literal["is", "is_not", "is_not_one_of", "is_one_of"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_6_OPERATOR_VALUES: set[
    EscalationPolicyPathRulesItemType9Type6Operator
] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_policy_path_rules_item_type_9_type_6_operator(
    value: str | None,
) -> EscalationPolicyPathRulesItemType9Type6Operator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_6_OPERATOR_VALUES:
        return cast(EscalationPolicyPathRulesItemType9Type6Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_6_OPERATOR_VALUES!r}"
    )
