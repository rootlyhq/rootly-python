from typing import Literal, cast

HeartbeatNotificationTargetType = Literal["EscalationPolicy", "Group", "Service", "User"]

HEARTBEAT_NOTIFICATION_TARGET_TYPE_VALUES: set[HeartbeatNotificationTargetType] = {
    "EscalationPolicy",
    "Group",
    "Service",
    "User",
}


def check_heartbeat_notification_target_type(value: str | None) -> HeartbeatNotificationTargetType | None:
    if value is None:
        return None
    if value in HEARTBEAT_NOTIFICATION_TARGET_TYPE_VALUES:
        return cast(HeartbeatNotificationTargetType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HEARTBEAT_NOTIFICATION_TARGET_TYPE_VALUES!r}")
