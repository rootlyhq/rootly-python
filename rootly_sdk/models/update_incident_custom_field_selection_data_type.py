from typing import Literal, cast

UpdateIncidentCustomFieldSelectionDataType = Literal["incident_custom_field_selections"]

UPDATE_INCIDENT_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES: set[UpdateIncidentCustomFieldSelectionDataType] = {
    "incident_custom_field_selections",
}


def check_update_incident_custom_field_selection_data_type(
    value: str | None,
) -> UpdateIncidentCustomFieldSelectionDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES:
        return cast(UpdateIncidentCustomFieldSelectionDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_CUSTOM_FIELD_SELECTION_DATA_TYPE_VALUES!r}"
    )
