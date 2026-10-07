from typing import Literal

NewSeverityDataType = Literal["severities"]

NEW_SEVERITY_DATA_TYPE_VALUES: set[NewSeverityDataType] = {
    "severities",
}


def check_new_severity_data_type(value: str | None) -> NewSeverityDataType | None:
    if value is None:
        return None
    if value in NEW_SEVERITY_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_SEVERITY_DATA_TYPE_VALUES!r}")
