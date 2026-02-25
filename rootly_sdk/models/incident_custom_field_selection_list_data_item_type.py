from typing import Literal, cast

IncidentCustomFieldSelectionListDataItemType = Literal["incident_custom_field_selections"]

INCIDENT_CUSTOM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentCustomFieldSelectionListDataItemType] = {
    "incident_custom_field_selections",
}


def check_incident_custom_field_selection_list_data_item_type(
    value: str | None,
) -> IncidentCustomFieldSelectionListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_CUSTOM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentCustomFieldSelectionListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_CUSTOM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
