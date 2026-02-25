from typing import Literal, cast

EscalationPolicyPathRulesItemType4Type1RuleType = Literal["working_hour"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_1_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType4Type1RuleType
] = {
    "working_hour",
}


def check_escalation_policy_path_rules_item_type_4_type_1_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType4Type1RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_1_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType4Type1RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_1_RULE_TYPE_VALUES!r}"
    )
