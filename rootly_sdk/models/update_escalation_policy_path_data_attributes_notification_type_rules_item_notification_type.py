from typing import Literal

UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType = Literal["audible", "quiet"]

UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType
] = {
    "audible",
    "quiet",
}


def check_update_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type(
    value: str | None,
) -> UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | None:
    if value is None:
        return None
    if value in UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
