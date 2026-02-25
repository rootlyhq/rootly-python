from typing import Literal, cast

AlertsSourceResponseDataType = Literal["alert_sources"]

ALERTS_SOURCE_RESPONSE_DATA_TYPE_VALUES: set[AlertsSourceResponseDataType] = {
    "alert_sources",
}


def check_alerts_source_response_data_type(value: str | None) -> AlertsSourceResponseDataType | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertsSourceResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_RESPONSE_DATA_TYPE_VALUES!r}")
