from typing import Literal, cast

PublishIncidentTaskParamsStatus = Literal[
    "completed", "identified", "in_progress", "investigating", "monitoring", "resolved", "scheduled"
]

PUBLISH_INCIDENT_TASK_PARAMS_STATUS_VALUES: set[PublishIncidentTaskParamsStatus] = {
    "completed",
    "identified",
    "in_progress",
    "investigating",
    "monitoring",
    "resolved",
    "scheduled",
}


def check_publish_incident_task_params_status(value: str | None) -> PublishIncidentTaskParamsStatus | None:
    if value is None:
        return None
    if value in PUBLISH_INCIDENT_TASK_PARAMS_STATUS_VALUES:
        return cast(PublishIncidentTaskParamsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUBLISH_INCIDENT_TASK_PARAMS_STATUS_VALUES!r}")
