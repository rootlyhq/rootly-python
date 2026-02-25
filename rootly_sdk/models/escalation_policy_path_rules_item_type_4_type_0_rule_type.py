from typing import Literal, cast

EscalationPolicyPathRulesItemType4Type0RuleType = Literal["alert_urgency"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_0_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType4Type0RuleType
] = {
    "alert_urgency",
}


def check_escalation_policy_path_rules_item_type_4_type_0_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType4Type0RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_0_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType4Type0RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_0_RULE_TYPE_VALUES!r}"
    )
