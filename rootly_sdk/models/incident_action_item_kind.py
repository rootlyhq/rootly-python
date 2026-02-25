from typing import Literal, cast

IncidentActionItemKind = Literal["follow_up", "task"]

INCIDENT_ACTION_ITEM_KIND_VALUES: set[IncidentActionItemKind] = {
    "follow_up",
    "task",
}


def check_incident_action_item_kind(value: str | None) -> IncidentActionItemKind | None:
    if value is None:
        return None
    if value in INCIDENT_ACTION_ITEM_KIND_VALUES:
        return cast(IncidentActionItemKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ACTION_ITEM_KIND_VALUES!r}")
