from typing import Literal, cast

IncidentRetrospectiveProgressStatus = Literal["active", "completed", "not_started", "skipped"]

INCIDENT_RETROSPECTIVE_PROGRESS_STATUS_VALUES: set[IncidentRetrospectiveProgressStatus] = {
    "active",
    "completed",
    "not_started",
    "skipped",
}


def check_incident_retrospective_progress_status(value: str | None) -> IncidentRetrospectiveProgressStatus | None:
    if value is None:
        return None
    if value in INCIDENT_RETROSPECTIVE_PROGRESS_STATUS_VALUES:
        return cast(IncidentRetrospectiveProgressStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_RETROSPECTIVE_PROGRESS_STATUS_VALUES!r}")
