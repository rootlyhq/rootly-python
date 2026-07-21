from typing import Literal, cast

EscalationPolicyPathRulesItemType6Operator = Literal["is", "is_not", "is_not_one_of", "is_one_of"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_OPERATOR_VALUES: set[EscalationPolicyPathRulesItemType6Operator] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_policy_path_rules_item_type_6_operator(
    value: str | None,
) -> EscalationPolicyPathRulesItemType6Operator | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_OPERATOR_VALUES:
        return cast(EscalationPolicyPathRulesItemType6Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_OPERATOR_VALUES!r}"
    )
