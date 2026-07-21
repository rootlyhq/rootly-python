from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType5RuleType = Literal["deferral_window"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType5RuleType
] = {
    "deferral_window",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_5_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType5RuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType5RuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_5_RULE_TYPE_VALUES!r}"
    )
