from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType = Literal["source"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType
] = {
    "source",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_rule_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES!r}"
    )
