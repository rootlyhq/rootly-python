from typing import Literal, cast

NewIncidentTypeDataType = Literal["incident_types"]

NEW_INCIDENT_TYPE_DATA_TYPE_VALUES: set[NewIncidentTypeDataType] = {
    "incident_types",
}


def check_new_incident_type_data_type(value: str | None) -> NewIncidentTypeDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_TYPE_DATA_TYPE_VALUES:
        return cast(NewIncidentTypeDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_TYPE_DATA_TYPE_VALUES!r}")
