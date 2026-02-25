from typing import Literal, cast

NewIncidentDataAttributesStatus = Literal[
    "acknowledged",
    "cancelled",
    "closed",
    "completed",
    "detected",
    "in_progress",
    "in_triage",
    "mitigated",
    "resolved",
    "scheduled",
    "started",
]

NEW_INCIDENT_DATA_ATTRIBUTES_STATUS_VALUES: set[NewIncidentDataAttributesStatus] = {
    "acknowledged",
    "cancelled",
    "closed",
    "completed",
    "detected",
    "in_progress",
    "in_triage",
    "mitigated",
    "resolved",
    "scheduled",
    "started",
}


def check_new_incident_data_attributes_status(value: str | None) -> NewIncidentDataAttributesStatus | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(NewIncidentDataAttributesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_DATA_ATTRIBUTES_STATUS_VALUES!r}")
