from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0RuleType = Literal["alert_urgency"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_0_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0RuleType
] = {
    "alert_urgency",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_9_type_0_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0RuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_0_RULE_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_0_RULE_TYPE_VALUES!r}"
    )
