from typing import Literal

AlertConfigurationDefaultUserNotificationSettingsAudibleContactTypesItem = Literal["call", "device", "email", "sms"]

ALERT_CONFIGURATION_DEFAULT_USER_NOTIFICATION_SETTINGS_AUDIBLE_CONTACT_TYPES_ITEM_VALUES: set[
    AlertConfigurationDefaultUserNotificationSettingsAudibleContactTypesItem
] = {
    "call",
    "device",
    "email",
    "sms",
}


def check_alert_configuration_default_user_notification_settings_audible_contact_types_item(
    value: str | None,
) -> AlertConfigurationDefaultUserNotificationSettingsAudibleContactTypesItem | None:
    if value is None:
        return None
    if value in ALERT_CONFIGURATION_DEFAULT_USER_NOTIFICATION_SETTINGS_AUDIBLE_CONTACT_TYPES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CONFIGURATION_DEFAULT_USER_NOTIFICATION_SETTINGS_AUDIBLE_CONTACT_TYPES_ITEM_VALUES!r}"
    )
