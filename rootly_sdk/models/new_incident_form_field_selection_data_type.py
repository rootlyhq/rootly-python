from typing import Literal, cast

NewIncidentFormFieldSelectionDataType = Literal["incident_form_field_selections"]

NEW_INCIDENT_FORM_FIELD_SELECTION_DATA_TYPE_VALUES: set[NewIncidentFormFieldSelectionDataType] = {
    "incident_form_field_selections",
}


def check_new_incident_form_field_selection_data_type(value: str | None) -> NewIncidentFormFieldSelectionDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_FORM_FIELD_SELECTION_DATA_TYPE_VALUES:
        return cast(NewIncidentFormFieldSelectionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_FORM_FIELD_SELECTION_DATA_TYPE_VALUES!r}"
    )
