from typing import Literal, cast

EscalationPolicyPathRulesItemType6RuleType = Literal["source"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_RULE_TYPE_VALUES: set[EscalationPolicyPathRulesItemType6RuleType] = {
    "source",
}


def check_escalation_policy_path_rules_item_type_6_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType6RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType6RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_RULE_TYPE_VALUES!r}"
    )
