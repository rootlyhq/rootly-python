from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType2RuleType = Literal["json_path"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_2_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType2RuleType
] = {
    "json_path",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_2_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType2RuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_2_RULE_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType2RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_2_RULE_TYPE_VALUES!r}"
    )
