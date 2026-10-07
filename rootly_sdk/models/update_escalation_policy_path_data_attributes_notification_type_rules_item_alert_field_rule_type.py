from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertFieldRuleType = Literal["field"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertFieldRuleType
] = {
    "field",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertFieldRuleType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_FIELD_RULE_TYPE_VALUES!r}"
    )
