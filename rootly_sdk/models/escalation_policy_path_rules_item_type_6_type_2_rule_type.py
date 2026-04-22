from typing import Literal, cast

EscalationPolicyPathRulesItemType6Type2RuleType = Literal["json_path"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_2_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType6Type2RuleType
] = {
    "json_path",
}


def check_escalation_policy_path_rules_item_type_6_type_2_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType6Type2RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_2_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType6Type2RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_6_TYPE_2_RULE_TYPE_VALUES!r}"
    )
