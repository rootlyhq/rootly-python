from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType = Literal["source"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType
] = {
    "source",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_rule_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_ALERT_SOURCE_RULE_TYPE_VALUES!r}"
    )
