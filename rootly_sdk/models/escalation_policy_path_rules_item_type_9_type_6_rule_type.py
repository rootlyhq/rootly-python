from typing import Literal, cast

EscalationPolicyPathRulesItemType9Type6RuleType = Literal["source"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_6_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType9Type6RuleType
] = {
    "source",
}


def check_escalation_policy_path_rules_item_type_9_type_6_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType9Type6RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_6_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType9Type6RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_9_TYPE_6_RULE_TYPE_VALUES!r}"
    )
