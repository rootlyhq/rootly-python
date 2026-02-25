from typing import Literal, cast

NewIncidentActionItemDataAttributesKind = Literal["follow_up", "task"]

NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_KIND_VALUES: set[NewIncidentActionItemDataAttributesKind] = {
    "follow_up",
    "task",
}


def check_new_incident_action_item_data_attributes_kind(value: str | None) -> NewIncidentActionItemDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(NewIncidentActionItemDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
