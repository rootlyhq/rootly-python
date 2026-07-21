from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7Operator = Literal["is_not_set", "is_set"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_7_OPERATOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7Operator
] = {
    "is_not_set",
    "is_set",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_9_type_7_operator(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7Operator | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_7_OPERATOR_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_9_TYPE_7_OPERATOR_VALUES!r}"
    )
