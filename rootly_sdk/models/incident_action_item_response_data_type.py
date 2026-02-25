from typing import Literal, cast

IncidentActionItemResponseDataType = Literal["incident_action_items"]

INCIDENT_ACTION_ITEM_RESPONSE_DATA_TYPE_VALUES: set[IncidentActionItemResponseDataType] = {
    "incident_action_items",
}


def check_incident_action_item_response_data_type(value: str | None) -> IncidentActionItemResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_ACTION_ITEM_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentActionItemResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ACTION_ITEM_RESPONSE_DATA_TYPE_VALUES!r}")
