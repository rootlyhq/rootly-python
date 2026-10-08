from typing import Literal

AlertsSourceSourceableAttributesType0NotificationTargetType = Literal[
    "EscalationPolicy", "Functionality", "Group", "Service", "User"
]

ALERTS_SOURCE_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES: set[
    AlertsSourceSourceableAttributesType0NotificationTargetType
] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
    "User",
}


def check_alerts_source_sourceable_attributes_type_0_notification_target_type(
    value: str | None,
) -> AlertsSourceSourceableAttributesType0NotificationTargetType | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES!r}"
    )
