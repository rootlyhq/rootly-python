from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType6Operator = Literal["is", "is_not", "is_not_one_of", "is_one_of"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_OPERATOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType6Operator
] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_6_operator(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType6Operator | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_OPERATOR_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType6Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_OPERATOR_VALUES!r}"
    )
