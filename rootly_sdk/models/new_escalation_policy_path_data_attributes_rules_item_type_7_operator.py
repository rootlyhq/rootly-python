from typing import Literal, cast

NewEscalationPolicyPathDataAttributesRulesItemType7Operator = Literal["is_not_set", "is_set"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_7_OPERATOR_VALUES: set[
    NewEscalationPolicyPathDataAttributesRulesItemType7Operator
] = {
    "is_not_set",
    "is_set",
}


def check_new_escalation_policy_path_data_attributes_rules_item_type_7_operator(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesRulesItemType7Operator | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_7_OPERATOR_VALUES:
        return cast(NewEscalationPolicyPathDataAttributesRulesItemType7Operator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_RULES_ITEM_TYPE_7_OPERATOR_VALUES!r}"
    )
