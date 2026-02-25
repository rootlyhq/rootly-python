from typing import Literal, cast

AlertResponseDataType = Literal["alerts"]

ALERT_RESPONSE_DATA_TYPE_VALUES: set[AlertResponseDataType] = {
    "alerts",
}


def check_alert_response_data_type(value: str | None) -> AlertResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_RESPONSE_DATA_TYPE_VALUES!r}")
