from typing import Literal, cast

InTriageIncidentDataType = Literal["incidents"]

IN_TRIAGE_INCIDENT_DATA_TYPE_VALUES: set[InTriageIncidentDataType] = {
    "incidents",
}


def check_in_triage_incident_data_type(value: str | None) -> InTriageIncidentDataType | None:
    if value is None:
        return None
    if value in IN_TRIAGE_INCIDENT_DATA_TYPE_VALUES:
        return cast(InTriageIncidentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IN_TRIAGE_INCIDENT_DATA_TYPE_VALUES!r}")
