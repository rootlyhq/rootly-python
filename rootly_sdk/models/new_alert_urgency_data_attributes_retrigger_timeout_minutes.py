from typing import Literal

NewAlertUrgencyDataAttributesRetriggerTimeoutMinutes = Literal[
    -1, 10, 20, 30, 40, 50, 60, 90, 120, 180, 240, 300, 360, 720, 1440
]

NEW_ALERT_URGENCY_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES: set[
    NewAlertUrgencyDataAttributesRetriggerTimeoutMinutes
] = {
    -1,
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


def check_new_alert_urgency_data_attributes_retrigger_timeout_minutes(
    value: int,
) -> NewAlertUrgencyDataAttributesRetriggerTimeoutMinutes:
    if value in NEW_ALERT_URGENCY_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_URGENCY_DATA_ATTRIBUTES_RETRIGGER_TIMEOUT_MINUTES_VALUES!r}"
    )
