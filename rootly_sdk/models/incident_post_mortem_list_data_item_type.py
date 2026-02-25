from typing import Literal, cast

IncidentPostMortemListDataItemType = Literal["incident_post_mortems"]

INCIDENT_POST_MORTEM_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentPostMortemListDataItemType] = {
    "incident_post_mortems",
}


def check_incident_post_mortem_list_data_item_type(value: str | None) -> IncidentPostMortemListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_POST_MORTEM_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentPostMortemListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_POST_MORTEM_LIST_DATA_ITEM_TYPE_VALUES!r}")
