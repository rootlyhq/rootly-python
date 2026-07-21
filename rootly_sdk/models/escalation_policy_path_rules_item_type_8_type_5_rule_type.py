from typing import Literal, cast

EscalationPolicyPathRulesItemType8Type5RuleType = Literal["deferral_window"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_8_TYPE_5_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType8Type5RuleType
] = {
    "deferral_window",
}


def check_escalation_policy_path_rules_item_type_8_type_5_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType8Type5RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_8_TYPE_5_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType8Type5RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_8_TYPE_5_RULE_TYPE_VALUES!r}"
    )
