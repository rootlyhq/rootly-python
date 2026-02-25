from typing import Literal, cast

IncidentFormFieldSelectionListDataItemType = Literal["incident_form_field_selections"]

INCIDENT_FORM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentFormFieldSelectionListDataItemType] = {
    "incident_form_field_selections",
}


def check_incident_form_field_selection_list_data_item_type(
    value: str | None,
) -> IncidentFormFieldSelectionListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_FORM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentFormFieldSelectionListDataItemType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_FORM_FIELD_SELECTION_LIST_DATA_ITEM_TYPE_VALUES!r}"
    )
