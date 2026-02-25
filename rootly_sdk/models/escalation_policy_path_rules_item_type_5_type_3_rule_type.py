from typing import Literal, cast

EscalationPolicyPathRulesItemType5Type3RuleType = Literal["field"]

ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_TYPE_3_RULE_TYPE_VALUES: set[
    EscalationPolicyPathRulesItemType5Type3RuleType
] = {
    "field",
}


def check_escalation_policy_path_rules_item_type_5_type_3_rule_type(
    value: str | None,
) -> EscalationPolicyPathRulesItemType5Type3RuleType | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_TYPE_3_RULE_TYPE_VALUES:
        return cast(EscalationPolicyPathRulesItemType5Type3RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_RULES_ITEM_TYPE_5_TYPE_3_RULE_TYPE_VALUES!r}"
    )
