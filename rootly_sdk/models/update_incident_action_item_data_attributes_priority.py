from typing import Literal, cast

UpdateIncidentActionItemDataAttributesPriority = Literal["high", "low", "medium"]

UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES: set[UpdateIncidentActionItemDataAttributesPriority] = {
    "high",
    "low",
    "medium",
}


def check_update_incident_action_item_data_attributes_priority(
    value: str | None,
) -> UpdateIncidentActionItemDataAttributesPriority | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return cast(UpdateIncidentActionItemDataAttributesPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES!r}"
    )
