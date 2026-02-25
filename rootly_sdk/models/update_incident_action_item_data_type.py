from typing import Literal, cast

UpdateIncidentActionItemDataType = Literal["incident_action_items"]

UPDATE_INCIDENT_ACTION_ITEM_DATA_TYPE_VALUES: set[UpdateIncidentActionItemDataType] = {
    "incident_action_items",
}


def check_update_incident_action_item_data_type(value: str | None) -> UpdateIncidentActionItemDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_ACTION_ITEM_DATA_TYPE_VALUES:
        return cast(UpdateIncidentActionItemDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_ACTION_ITEM_DATA_TYPE_VALUES!r}")
