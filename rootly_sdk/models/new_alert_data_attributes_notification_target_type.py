from typing import Literal

NewAlertDataAttributesNotificationTargetType = Literal["EscalationPolicy", "Functionality", "Group", "Service", "User"]

NEW_ALERT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES: set[NewAlertDataAttributesNotificationTargetType] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
    "User",
}


def check_new_alert_data_attributes_notification_target_type(
    value: str | None,
) -> NewAlertDataAttributesNotificationTargetType | None:
    if value is None:
        return None
    if value in NEW_ALERT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES!r}"
    )
