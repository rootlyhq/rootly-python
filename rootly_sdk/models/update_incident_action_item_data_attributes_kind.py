from typing import Literal, cast

UpdateIncidentActionItemDataAttributesKind = Literal["follow_up", "task"]

UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateIncidentActionItemDataAttributesKind] = {
    "follow_up",
    "task",
}


def check_update_incident_action_item_data_attributes_kind(
    value: str | None,
) -> UpdateIncidentActionItemDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateIncidentActionItemDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
