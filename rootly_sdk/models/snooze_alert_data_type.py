from typing import Literal, cast

SnoozeAlertDataType = Literal["alerts"]

SNOOZE_ALERT_DATA_TYPE_VALUES: set[SnoozeAlertDataType] = {
    "alerts",
}


def check_snooze_alert_data_type(value: str | None) -> SnoozeAlertDataType | None:
    if value is None:
        return None
    if value in SNOOZE_ALERT_DATA_TYPE_VALUES:
        return cast(SnoozeAlertDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SNOOZE_ALERT_DATA_TYPE_VALUES!r}")
