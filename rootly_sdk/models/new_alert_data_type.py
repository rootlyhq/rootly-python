from typing import Literal, cast

NewAlertDataType = Literal["alerts"]

NEW_ALERT_DATA_TYPE_VALUES: set[NewAlertDataType] = {
    "alerts",
}


def check_new_alert_data_type(value: str | None) -> NewAlertDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_DATA_TYPE_VALUES:
        return cast(NewAlertDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_DATA_TYPE_VALUES!r}")
