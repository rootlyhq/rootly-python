from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2RuleType = Literal["json_path"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_2_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2RuleType
] = {
    "json_path",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_9_type_2_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2RuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_2_RULE_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_2_RULE_TYPE_VALUES!r}"
    )
