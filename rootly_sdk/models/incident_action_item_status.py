from typing import Literal

IncidentActionItemStatus = Literal["cancelled", "done", "in_progress", "open"]

INCIDENT_ACTION_ITEM_STATUS_VALUES: set[IncidentActionItemStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_incident_action_item_status(value: str | None) -> IncidentActionItemStatus | None:
    if value is None:
        return None
    if value in INCIDENT_ACTION_ITEM_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ACTION_ITEM_STATUS_VALUES!r}")
