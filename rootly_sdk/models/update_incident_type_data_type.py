from typing import Literal, cast

UpdateIncidentTypeDataType = Literal["incident_types"]

UPDATE_INCIDENT_TYPE_DATA_TYPE_VALUES: set[UpdateIncidentTypeDataType] = {
    "incident_types",
}


def check_update_incident_type_data_type(value: str | None) -> UpdateIncidentTypeDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_TYPE_DATA_TYPE_VALUES:
        return cast(UpdateIncidentTypeDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_TYPE_DATA_TYPE_VALUES!r}")
