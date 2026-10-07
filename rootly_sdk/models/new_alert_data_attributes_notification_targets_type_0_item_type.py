from typing import Literal

NewAlertDataAttributesNotificationTargetsType0ItemType = Literal[
    "EscalationPolicy", "Functionality", "Group", "Service", "User"
]

NEW_ALERT_DATA_ATTRIBUTES_NOTIFICATION_TARGETS_TYPE_0_ITEM_TYPE_VALUES: set[
    NewAlertDataAttributesNotificationTargetsType0ItemType
] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
    "User",
}


def check_new_alert_data_attributes_notification_targets_type_0_item_type(
    value: str | None,
) -> NewAlertDataAttributesNotificationTargetsType0ItemType | None:
    if value is None:
        return None
    if value in NEW_ALERT_DATA_ATTRIBUTES_NOTIFICATION_TARGETS_TYPE_0_ITEM_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_DATA_ATTRIBUTES_NOTIFICATION_TARGETS_TYPE_0_ITEM_TYPE_VALUES!r}"
    )
