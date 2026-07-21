from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType1RuleType = Literal["working_hour"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_1_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType1RuleType
] = {
    "working_hour",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_1_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType1RuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_1_RULE_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType1RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_1_RULE_TYPE_VALUES!r}"
    )
