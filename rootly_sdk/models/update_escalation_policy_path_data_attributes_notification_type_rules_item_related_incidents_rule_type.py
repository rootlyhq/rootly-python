from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsRuleType = Literal["related_incidents"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsRuleType
] = {
    "related_incidents",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_related_incidents_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidentsRuleType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_RULE_TYPE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_RELATED_INCIDENTS_RULE_TYPE_VALUES!r}"
    )
