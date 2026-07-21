from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType3Operator = Literal[
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

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_OPERATOR_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType3Operator
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


def check_new_escalation_policy_path_data_attributes_rules_item_type_3_operator(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType3Operator | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_OPERATOR_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType3Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_3_OPERATOR_VALUES!r}"
    )
