from typing import Literal, cast

IncidentRetrospectiveStepStatus = Literal["completed", "in_progress", "skipped", "todo"]

INCIDENT_RETROSPECTIVE_STEP_STATUS_VALUES: set[IncidentRetrospectiveStepStatus] = {
    "completed",
    "in_progress",
    "skipped",
    "todo",
}


def check_incident_retrospective_step_status(value: str | None) -> IncidentRetrospectiveStepStatus | None:
    if value is None:
        return None
    if value in INCIDENT_RETROSPECTIVE_STEP_STATUS_VALUES:
        return cast(IncidentRetrospectiveStepStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_RETROSPECTIVE_STEP_STATUS_VALUES!r}")
