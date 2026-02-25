from typing import Literal, cast

IncidentActionItemPriority = Literal["high", "low", "medium"]

INCIDENT_ACTION_ITEM_PRIORITY_VALUES: set[IncidentActionItemPriority] = {
    "high",
    "low",
    "medium",
}


def check_incident_action_item_priority(value: str | None) -> IncidentActionItemPriority | None:
    if value is None:
        return None
    if value in INCIDENT_ACTION_ITEM_PRIORITY_VALUES:
        return cast(IncidentActionItemPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ACTION_ITEM_PRIORITY_VALUES!r}")
