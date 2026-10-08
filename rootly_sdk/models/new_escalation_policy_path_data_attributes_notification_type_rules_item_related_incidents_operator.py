from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsOperator = Literal["is_not_set", "is_set"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsOperator
] = {
    "is_not_set",
    "is_set",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_related_incidents_operator(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsOperator | None:
    if value is None:
        return None
    if (
        value
        in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES!r}"
    )
