from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3Operator = Literal[
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_empty",
    "is_not",
    "is_not_empty",
    "is_not_one_of",
    "is_one_of",
    "matches",
    "starts_with",
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_8_TYPE_3_OPERATOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3Operator
] = {
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_empty",
    "is_not",
    "is_not_empty",
    "is_not_one_of",
    "is_one_of",
    "matches",
    "starts_with",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_8_type_3_operator(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3Operator | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_8_TYPE_3_OPERATOR_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_8_TYPE_3_OPERATOR_VALUES!r}"
    )
