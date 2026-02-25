from typing import Literal, cast

UpdateAlertFieldDataType = Literal["alert_fields"]

UPDATE_ALERT_FIELD_DATA_TYPE_VALUES: set[UpdateAlertFieldDataType] = {
    "alert_fields",
}


def check_update_alert_field_data_type(value: str | None) -> UpdateAlertFieldDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_FIELD_DATA_TYPE_VALUES:
        return cast(UpdateAlertFieldDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_FIELD_DATA_TYPE_VALUES!r}")
