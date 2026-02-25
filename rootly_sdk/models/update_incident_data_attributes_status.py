from typing import Literal, cast

UpdateIncidentDataAttributesStatus = Literal[
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

UPDATE_INCIDENT_DATA_ATTRIBUTES_STATUS_VALUES: set[UpdateIncidentDataAttributesStatus] = {
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


def check_update_incident_data_attributes_status(value: str | None) -> UpdateIncidentDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(UpdateIncidentDataAttributesStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_DATA_ATTRIBUTES_STATUS_VALUES!r}")
