from typing import Literal

NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType = Literal["audible", "quiet"]

NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES: set[
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType
] = {
    "audible",
    "quiet",
}


def check_new_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type(
    value: str | None,
) -> NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | None:
    if value is None:
        return None
    if value in NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ESCALATION_POLICY_PATH_DATA_ATTRIBUTES_NOTIFICATION_TYPE_RULES_ITEM_NOTIFICATION_TYPE_VALUES!r}"
    )
