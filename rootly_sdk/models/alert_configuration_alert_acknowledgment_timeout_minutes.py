from typing import Literal

AlertConfigurationAlertAcknowledgmentTimeoutMinutes = Literal[
    10, 20, 30, 40, 50, 60, 90, 120, 180, 240, 300, 360, 720, 1440
]

ALERT_CONFIGURATION_ALERT_ACKNOWLEDGMENT_TIMEOUT_MINUTES_VALUES: set[
    AlertConfigurationAlertAcknowledgmentTimeoutMinutes
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


def check_alert_configuration_alert_acknowledgment_timeout_minutes(
    value: int,
) -> AlertConfigurationAlertAcknowledgmentTimeoutMinutes:
    if value in ALERT_CONFIGURATION_ALERT_ACKNOWLEDGMENT_TIMEOUT_MINUTES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CONFIGURATION_ALERT_ACKNOWLEDGMENT_TIMEOUT_MINUTES_VALUES!r}"
    )
