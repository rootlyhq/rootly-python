from typing import Literal

NewAlertsSourceDataAttributesSourceableAttributesType0NotificationTargetType = Literal[
    "EscalationPolicy", "Functionality", "Group", "Service", "User"
]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES: set[
    NewAlertsSourceDataAttributesSourceableAttributesType0NotificationTargetType
] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
    "User",
}


def check_new_alerts_source_data_attributes_sourceable_attributes_type_0_notification_target_type(
    value: str | None,
) -> NewAlertsSourceDataAttributesSourceableAttributesType0NotificationTargetType | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES!r}"
    )
