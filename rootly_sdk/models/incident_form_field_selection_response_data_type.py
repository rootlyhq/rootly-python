from typing import Literal, cast

IncidentFormFieldSelectionResponseDataType = Literal["incident_form_field_selections"]

INCIDENT_FORM_FIELD_SELECTION_RESPONSE_DATA_TYPE_VALUES: set[IncidentFormFieldSelectionResponseDataType] = {
    "incident_form_field_selections",
}


def check_incident_form_field_selection_response_data_type(value: str | None) -> IncidentFormFieldSelectionResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_FORM_FIELD_SELECTION_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentFormFieldSelectionResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_FORM_FIELD_SELECTION_RESPONSE_DATA_TYPE_VALUES!r}"
    )
