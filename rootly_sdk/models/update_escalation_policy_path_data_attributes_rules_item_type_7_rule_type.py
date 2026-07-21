from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType7RuleType = Literal["related_incidents"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_7_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType7RuleType
] = {
    "related_incidents",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_7_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType7RuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_7_RULE_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType7RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_7_RULE_TYPE_VALUES!r}"
    )
