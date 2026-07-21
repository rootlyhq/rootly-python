from typing import Literal, cast

EscalationPolicyPathRulesItemType5RuleType = Literal["deferral_window"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES: set[EscalationPolicyPathRulesItemType5RuleType] = {
    "deferral_window",
}


def check_escalation_policy_path_rules_item_type_5_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType5RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType5RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES!r}"
    )
