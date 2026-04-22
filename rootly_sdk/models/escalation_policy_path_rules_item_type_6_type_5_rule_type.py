from typing import Literal, cast

EscalationPolicyPathRulesItemType6Type5RuleType = Literal["deferral_window"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_5_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType6Type5RuleType
] = {
    "deferral_window",
}


def check_escalation_policy_path_rules_item_type_6_type_5_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType6Type5RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_5_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType6Type5RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_5_RULE_TYPE_VALUES!r}"
    )
