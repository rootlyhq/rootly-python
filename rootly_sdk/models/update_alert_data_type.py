from typing import Literal

UpdateAlertDataType = Literal["alerts"]

UPDATE_ALERT_DATA_TYPE_VALUES: set[UpdateAlertDataType] = {
    "alerts",
}


def check_update_alert_data_type(value: str | None) -> UpdateAlertDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_DATA_TYPE_VALUES!r}")
