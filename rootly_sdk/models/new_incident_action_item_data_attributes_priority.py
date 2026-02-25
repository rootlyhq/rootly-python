from typing import Literal, cast

NewIncidentActionItemDataAttributesPriority = Literal["high", "low", "medium"]

NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES: set[NewIncidentActionItemDataAttributesPriority] = {
    "high",
    "low",
    "medium",
}


def check_new_incident_action_item_data_attributes_priority(
    value: str | None,
) -> NewIncidentActionItemDataAttributesPriority | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return cast(NewIncidentActionItemDataAttributesPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES!r}"
    )
