from typing import Literal, cast

UpdateIncidentFormFieldSelectionDataType = Literal["incident_form_field_selections"]

UPDATE_INCIDENT_FORM_FIELD_SELECTION_DATA_TYPE_VALUES: set[UpdateIncidentFormFieldSelectionDataType] = {
    "incident_form_field_selections",
}


def check_update_incident_form_field_selection_data_type(value: str | None) -> UpdateIncidentFormFieldSelectionDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_FORM_FIELD_SELECTION_DATA_TYPE_VALUES:
        return cast(UpdateIncidentFormFieldSelectionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_FORM_FIELD_SELECTION_DATA_TYPE_VALUES!r}"
    )
