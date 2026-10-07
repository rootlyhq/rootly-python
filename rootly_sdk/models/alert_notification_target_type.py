from typing import Literal

AlertNotificationTargetType = Literal["EscalationPolicy", "Functionality", "Group", "Service", "User"]

ALERT_NOTIFICATION_TARGET_TYPE_VALUES: set[AlertNotificationTargetType] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
    "User",
}


def check_alert_notification_target_type(value: str | None) -> AlertNotificationTargetType | None:
    if value is None:
        return None
    if value in ALERT_NOTIFICATION_TARGET_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_NOTIFICATION_TARGET_TYPE_VALUES!r}")
