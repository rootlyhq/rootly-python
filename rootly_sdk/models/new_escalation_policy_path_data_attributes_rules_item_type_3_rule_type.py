from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType3RuleType = Literal["field"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType3RuleType
] = {
    "field",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_3_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType3RuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_RULE_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType3RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_RULE_TYPE_VALUES!r}"
    )
