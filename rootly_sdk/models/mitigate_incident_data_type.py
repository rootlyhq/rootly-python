from typing import Literal, cast

MitigateIncidentDataType = Literal["incidents"]

MITIGATE_INCIDENT_DATA_TYPE_VALUES: set[MitigateIncidentDataType] = {
    "incidents",
}


def check_mitigate_incident_data_type(value: str | None) -> MitigateIncidentDataType | None:
    if value is None:
        return None
    if value in MITIGATE_INCIDENT_DATA_TYPE_VALUES:
        return cast(MitigateIncidentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MITIGATE_INCIDENT_DATA_TYPE_VALUES!r}")
