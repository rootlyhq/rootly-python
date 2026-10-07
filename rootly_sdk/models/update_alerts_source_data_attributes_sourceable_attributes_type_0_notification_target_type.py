from typing import Literal

UpdateAlertsSourceDataAttributesSourceableAttributesType0NotificationTargetType = Literal[
    "EscalationPolicy", "Functionality", "Group", "Service", "User"
]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES: set[
    UpdateAlertsSourceDataAttributesSourceableAttributesType0NotificationTargetType
] = {
    "EscalationPolicy",
    "Functionality",
    "Group",
    "Service",
    "User",
}


def check_update_alerts_source_data_attributes_sourceable_attributes_type_0_notification_target_type(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesSourceableAttributesType0NotificationTargetType | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCEABLE_ATTRIBUTES_TYPE_0_NOTIFICATION_TARGET_TYPE_VALUES!r}"
    )
