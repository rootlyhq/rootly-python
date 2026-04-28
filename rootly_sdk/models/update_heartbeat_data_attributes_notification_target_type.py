from typing import Literal, cast

UpdateHeartbeatDataAttributesNotificationTargetType = Literal[
    "EscalationPolicy", "Functionality", "Group", "Service", "User"
]

UPDATE_HEARTBEAT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES: set[
    UpdateHeartbeatDataAttributesNotificationTargetType
] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
    "User",
}


def check_update_heartbeat_data_attributes_notification_target_type(
    value: str | None,
) -> UpdateHeartbeatDataAttributesNotificationTargetType | None:
    if value is None:
        return None
    if value in UPDATE_HEARTBEAT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES:
        return cast(UpdateHeartbeatDataAttributesNotificationTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_HEARTBEAT_DATA_ATTRIBUTES_NOTIFICATION_TARGET_TYPE_VALUES!r}"
    )
