from typing import Literal

PublishIncidentTaskParamsSyncedComponentStatus = Literal[
    "degraded_performance", "major_outage", "operational", "partial_outage"
]

PUBLISH_INCIDENT_TASK_PARAMS_SYNCED_COMPONENT_STATUS_VALUES: set[PublishIncidentTaskParamsSyncedComponentStatus] = {
    "degraded_performance",
    "major_outage",
    "operational",
    "partial_outage",
}


def check_publish_incident_task_params_synced_component_status(
    value: str | None,
) -> PublishIncidentTaskParamsSyncedComponentStatus | None:
    if value is None:
        return None
    if value in PUBLISH_INCIDENT_TASK_PARAMS_SYNCED_COMPONENT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISH_INCIDENT_TASK_PARAMS_SYNCED_COMPONENT_STATUS_VALUES!r}"
    )
