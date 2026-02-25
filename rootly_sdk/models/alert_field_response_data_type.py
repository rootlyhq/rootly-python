from typing import Literal, cast

AlertFieldResponseDataType = Literal["alert_fields"]

ALERT_FIELD_RESPONSE_DATA_TYPE_VALUES: set[AlertFieldResponseDataType] = {
    "alert_fields",
}


def check_alert_field_response_data_type(value: str | None) -> AlertFieldResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_FIELD_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertFieldResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_FIELD_RESPONSE_DATA_TYPE_VALUES!r}")
