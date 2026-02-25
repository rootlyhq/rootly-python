from typing import Literal, cast

IncidentTriggerParamsIncidentStatusesItem = Literal[
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

INCIDENT_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES: set[IncidentTriggerParamsIncidentStatusesItem] = {
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


def check_incident_trigger_params_incident_statuses_item(
    value: str | None,
) -> IncidentTriggerParamsIncidentStatusesItem | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES:
        return cast(IncidentTriggerParamsIncidentStatusesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES!r}"
    )
