from typing import Literal, cast

EscalationPolicyPathRulesItemType9Type7Operator = Literal["is_not_set", "is_set"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_7_OPERATOR_VALUES: set[
    EscalationPolicyPathRulesItemType9Type7Operator
] = {
    "is_not_set",
    "is_set",
}


def check_escalation_policy_path_rules_item_type_9_type_7_operator(
    value: str | None,
) -> EscalationPolicyPathRulesItemType9Type7Operator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_7_OPERATOR_VALUES:
        return cast(EscalationPolicyPathRulesItemType9Type7Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_7_OPERATOR_VALUES!r}"
    )
