from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsOperator = Literal[
    "is_not_set", "is_set"
]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsOperator
] = {
    "is_not_set",
    "is_set",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_related_incidents_operator(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsOperator | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_OPERATOR_VALUES!r}"
    )
