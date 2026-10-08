from typing import Literal

ResolveIncidentDataType = Literal["incidents"]

RESOLVE_INCIDENT_DATA_TYPE_VALUES: set[ResolveIncidentDataType] = {
    "incidents",
}


def check_resolve_incident_data_type(value: str | None) -> ResolveIncidentDataType | None:
    if value is None:
        return None
    if value in RESOLVE_INCIDENT_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESOLVE_INCIDENT_DATA_TYPE_VALUES!r}")
