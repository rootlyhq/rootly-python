from typing import Literal, cast

RestartIncidentDataType = Literal["incidents"]

RESTART_INCIDENT_DATA_TYPE_VALUES: set[RestartIncidentDataType] = {
    "incidents",
}


def check_restart_incident_data_type(value: str | None) -> RestartIncidentDataType | None:
    if value is None:
        return None
    if value in RESTART_INCIDENT_DATA_TYPE_VALUES:
        return cast(RestartIncidentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESTART_INCIDENT_DATA_TYPE_VALUES!r}")
