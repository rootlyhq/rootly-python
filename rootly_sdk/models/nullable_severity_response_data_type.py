from typing import Literal

NullableSeverityResponseDataType = Literal["severities"]

NULLABLE_SEVERITY_RESPONSE_DATA_TYPE_VALUES: set[NullableSeverityResponseDataType] = {
    "severities",
}


def check_nullable_severity_response_data_type(value: str | None) -> NullableSeverityResponseDataType | None:
    if value is None:
        return None
    if value in NULLABLE_SEVERITY_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NULLABLE_SEVERITY_RESPONSE_DATA_TYPE_VALUES!r}")
