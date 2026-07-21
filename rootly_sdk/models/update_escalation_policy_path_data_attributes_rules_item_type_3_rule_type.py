from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType3RuleType = Literal["field"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType3RuleType
] = {
    "field",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_3_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType3RuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_RULE_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType3RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_RULE_TYPE_VALUES!r}"
    )
