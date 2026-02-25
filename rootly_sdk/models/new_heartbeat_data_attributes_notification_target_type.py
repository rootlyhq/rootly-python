from typing import Literal, cast

NewHeartbeatDataAttributesNotificationTargetType = Literal["EscalationPolicy", "Group", "Service", "User"]

NEW_HEARTBEAT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES: set[NewHeartbeatDataAttributesNotificationTargetType] = {
    "EscalationPolicy",
    "Group",
    "Service",
    "User",
}


def check_new_heartbeat_data_attributes_notification_target_type(
    value: str | None,
) -> NewHeartbeatDataAttributesNotificationTargetType | None:
    if value is None:
        return None
    if value in NEW_HEARTBEAT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES:
        return cast(NewHeartbeatDataAttributesNotificationTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_HEARTBEAT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES!r}"
    )
