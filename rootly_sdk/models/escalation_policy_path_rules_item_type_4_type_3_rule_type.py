from typing import Literal, cast

EscalationPolicyPathRulesItemType4Type3RuleType = Literal["field"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_3_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType4Type3RuleType
] = {
    "field",
}


def check_escalation_policy_path_rules_item_type_4_type_3_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType4Type3RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_3_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType4Type3RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_4_TYPE_3_RULE_TYPE_VALUES!r}"
    )
