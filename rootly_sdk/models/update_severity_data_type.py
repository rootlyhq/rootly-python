from typing import Literal, cast

UpdateSeverityDataType = Literal["severities"]

UPDATE_SEVERITY_DATA_TYPE_VALUES: set[UpdateSeverityDataType] = {
    "severities",
}


def check_update_severity_data_type(value: str | None) -> UpdateSeverityDataType | None:
    if value is None:
        return None
    if value in UPDATE_SEVERITY_DATA_TYPE_VALUES:
        return cast(UpdateSeverityDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_SEVERITY_DATA_TYPE_VALUES!r}")
