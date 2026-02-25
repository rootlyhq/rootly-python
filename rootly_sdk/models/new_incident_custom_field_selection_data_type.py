from typing import Literal, cast

NewIncidentCustomFieldSelectionDataType = Literal["incident_custom_field_selections"]

NEW_INCIDENT_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES: set[NewIncidentCustomFieldSelectionDataType] = {
    "incident_custom_field_selections",
}


def check_new_incident_custom_field_selection_data_type(value: str | None) -> NewIncidentCustomFieldSelectionDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES:
        return cast(NewIncidentCustomFieldSelectionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES!r}"
    )
