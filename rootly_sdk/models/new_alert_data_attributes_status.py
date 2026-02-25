from typing import Literal, cast

NewAlertDataAttributesStatus = Literal["open", "triggered"]

NEW_ALERT_DATA_ATTRIBUTES_STATUS_VALUES: set[NewAlertDataAttributesStatus] = {
    "open",
    "triggered",
}


def check_new_alert_data_attributes_status(value: str | None) -> NewAlertDataAttributesStatus | None:
    if value is None:
        return None
    if value in NEW_ALERT_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(NewAlertDataAttributesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_DATA_ATTRIBUTES_STATUS_VALUES!r}")
