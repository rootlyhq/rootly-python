from typing import Literal, cast

UpdateEscalationPolicyPathDataAttributesRulesItemType2Operator = Literal[
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_not",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches",
    "starts_with",
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_2_OPERATOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesRulesItemType2Operator
] = {
    "contains",
    "contains_key",
    "does_not_contain",
    "does_not_contain_key",
    "does_not_match",
    "does_not_start_with",
    "is",
    "is_not",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches",
    "starts_with",
}


def check_update_escalation_policy_path_data_attributes_rules_item_type_2_operator(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesRulesItemType2Operator | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_2_OPERATOR_VALUES:
        return cast(UpdateEscalationPolicyPathDataAttributesRulesItemType2Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_2_OPERATOR_VALUES!r}"
    )
