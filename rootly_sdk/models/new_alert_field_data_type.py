from typing import Literal, cast

NewAlertFieldDataType = Literal["alert_fields"]

NEW_ALERT_FIELD_DATA_TYPE_VALUES: set[NewAlertFieldDataType] = {
    "alert_fields",
}


def check_new_alert_field_data_type(value: str | None) -> NewAlertFieldDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_FIELD_DATA_TYPE_VALUES:
        return cast(NewAlertFieldDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_FIELD_DATA_TYPE_VALUES!r}")
