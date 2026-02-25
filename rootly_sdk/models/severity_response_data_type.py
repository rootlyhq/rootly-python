from typing import Literal, cast

SeverityResponseDataType = Literal["severities"]

SEVERITY_RESPONSE_DATA_TYPE_VALUES: set[SeverityResponseDataType] = {
    "severities",
}


def check_severity_response_data_type(value: str | None) -> SeverityResponseDataType | None:
    if value is None:
        return None
    if value in SEVERITY_RESPONSE_DATA_TYPE_VALUES:
        return cast(SeverityResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEVERITY_RESPONSE_DATA_TYPE_VALUES!r}")
