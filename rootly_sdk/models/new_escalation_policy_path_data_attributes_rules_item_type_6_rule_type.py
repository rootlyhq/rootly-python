from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType6RuleType = Literal["source"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType6RuleType
] = {
    "source",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_6_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType6RuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_RULE_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType6RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_RULE_TYPE_VALUES!r}"
    )
