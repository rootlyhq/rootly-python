from typing import Literal, cast

NewIncidentActionItemDataType = Literal["incident_action_items"]

NEW_INCIDENT_ACTION_ITEM_DATA_TYPE_VALUES: set[NewIncidentActionItemDataType] = {
    "incident_action_items",
}


def check_new_incident_action_item_data_type(value: str | None) -> NewIncidentActionItemDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_ACTION_ITEM_DATA_TYPE_VALUES:
        return cast(NewIncidentActionItemDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_ACTION_ITEM_DATA_TYPE_VALUES!r}")
