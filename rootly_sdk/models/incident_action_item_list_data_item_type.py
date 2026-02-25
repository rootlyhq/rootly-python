from typing import Literal, cast

IncidentActionItemListDataItemType = Literal["incident_action_items"]

INCIDENT_ACTION_ITEM_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentActionItemListDataItemType] = {
    "incident_action_items",
}


def check_incident_action_item_list_data_item_type(value: str | None) -> IncidentActionItemListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_ACTION_ITEM_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentActionItemListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_ACTION_ITEM_LIST_DATA_ITEM_TYPE_VALUES!r}")
