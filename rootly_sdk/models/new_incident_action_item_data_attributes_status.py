from typing import Literal

NewIncidentActionItemDataAttributesStatus = Literal["cancelled", "done", "in_progress", "open"]

NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES: set[NewIncidentActionItemDataAttributesStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_new_incident_action_item_data_attributes_status(
    value: str | None,
) -> NewIncidentActionItemDataAttributesStatus | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
