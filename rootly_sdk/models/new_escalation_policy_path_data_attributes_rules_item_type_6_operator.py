from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType6Operator = Literal["is", "is_not", "is_not_one_of", "is_one_of"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_OPERATOR_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType6Operator
] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_6_operator(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType6Operator | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_OPERATOR_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType6Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_6_OPERATOR_VALUES!r}"
    )
