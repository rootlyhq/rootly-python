from typing import Literal

ActionItemTriggerParamsIncidentStatusesItem = Literal[
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

ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES: set[ActionItemTriggerParamsIncidentStatusesItem] = {
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


def check_action_item_trigger_params_incident_statuses_item(
    value: str | None,
) -> ActionItemTriggerParamsIncidentStatusesItem | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_INCIDENT_STATUSES_ITEM_VALUES!r}"
    )
