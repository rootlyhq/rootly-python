from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType0RuleType = Literal["alert_urgency"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_0_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType0RuleType
] = {
    "alert_urgency",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_0_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType0RuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_0_RULE_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType0RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_0_RULE_TYPE_VALUES!r}"
    )
