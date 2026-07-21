from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType5RuleType = Literal["deferral_window"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType5RuleType
] = {
    "deferral_window",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_5_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType5RuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType5RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES!r}"
    )
