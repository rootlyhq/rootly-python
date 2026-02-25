from typing import Literal, cast

UpdateIncidentActionItemDataAttributesStatus = Literal["cancelled", "done", "in_progress", "open"]

UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES: set[UpdateIncidentActionItemDataAttributesStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_update_incident_action_item_data_attributes_status(
    value: str | None,
) -> UpdateIncidentActionItemDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(UpdateIncidentActionItemDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
