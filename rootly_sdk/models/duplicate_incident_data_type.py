from typing import Literal, cast

DuplicateIncidentDataType = Literal["incidents"]

DUPLICATE_INCIDENT_DATA_TYPE_VALUES: set[DuplicateIncidentDataType] = {
    "incidents",
}


def check_duplicate_incident_data_type(value: str | None) -> DuplicateIncidentDataType | None:
    if value is None:
        return None
    if value in DUPLICATE_INCIDENT_DATA_TYPE_VALUES:
        return cast(DuplicateIncidentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_INCIDENT_DATA_TYPE_VALUES!r}")
