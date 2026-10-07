from typing import Literal

UpdateAlertConfigurationDataAttributesAlertAcknowledgmentTimeoutMinutes = Literal[
    10, 20, 30, 40, 50, 60, 90, 120, 180, 240, 300, 360, 720, 1440
]

UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_ALERT_ACKNOWLEDGMENT_TIMEOUT_MINUTES_VALUES: set[
    UpdateAlertConfigurationDataAttributesAlertAcknowledgmentTimeoutMinutes
] = {
    10,
    20,
    30,
    40,
    50,
    60,
    90,
    120,
    180,
    240,
    300,
    360,
    720,
    1440,
}


def check_update_alert_configuration_data_attributes_alert_acknowledgment_timeout_minutes(
    value: int,
) -> UpdateAlertConfigurationDataAttributesAlertAcknowledgmentTimeoutMinutes:
    if value in UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_ALERT_ACKNOWLEDGMENT_TIMEOUT_MINUTES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_CONFIGURATION_DATA_ATTRIBUTES_ALERT_ACKNOWLEDGMENT_TIMEOUT_MINUTES_VALUES!r}"
    )
