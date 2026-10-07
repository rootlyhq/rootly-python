from typing import Literal

AlertConfigurationDefaultUserNotificationSettingsQuietContactTypesItem = Literal[
    "call", "email", "non_critical_device", "sms"
]

ALERT_CONFIGURATION_DEFAULT_USER_NOTIFICATION_SETTINGS_QUIET_CONTACT_TYPES_ITEM_VALUES: set[
    AlertConfigurationDefaultUserNotificationSettingsQuietContactTypesItem
] = {
    "call",
    "email",
    "non_critical_device",
    "sms",
}


def check_alert_configuration_default_user_notification_settings_quiet_contact_types_item(
    value: str | None,
) -> AlertConfigurationDefaultUserNotificationSettingsQuietContactTypesItem | None:
    if value is None:
        return None
    if value in ALERT_CONFIGURATION_DEFAULT_USER_NOTIFICATION_SETTINGS_QUIET_CONTACT_TYPES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CONFIGURATION_DEFAULT_USER_NOTIFICATION_SETTINGS_QUIET_CONTACT_TYPES_ITEM_VALUES!r}"
    )
