from typing import Literal

UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsQuietContactTypesItem = Literal[
    "call", "email", "non_critical_device", "sms"
]

UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_DEFAULT_USER_NOTIFICATION_SETTINGS_QUIET_CONTACT_TYPES_ITEM_VALUES: set[
    UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsQuietContactTypesItem
] = {
    "call",
    "email",
    "non_critical_device",
    "sms",
}


def check_update_alert_configuration_data_attributes_default_user_notification_settings_quiet_contact_types_item(
    value: str | None,
) -> UpdateAlertConfigurationDataAttributesDefaultUserNotificationSettingsQuietContactTypesItem | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_DEFAULT_USER_NOTIFICATION_SETTINGS_QUIET_CONTACT_TYPES_ITEM_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_DEFAULT_USER_NOTIFICATION_SETTINGS_QUIET_CONTACT_TYPES_ITEM_VALUES!r}"
    )
