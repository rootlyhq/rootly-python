from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType1RuleType = Literal["working_hour"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_1_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType1RuleType
] = {
    "working_hour",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_1_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType1RuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_1_RULE_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType1RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_1_RULE_TYPE_VALUES!r}"
    )
