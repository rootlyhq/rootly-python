from typing import Literal, cast

UpdateIncidentDataType = Literal["incidents"]

UPDATE_INCIDENT_DATA_TYPE_VALUES: set[UpdateIncidentDataType] = {
    "incidents",
}


def check_update_incident_data_type(value: str | None) -> UpdateIncidentDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_DATA_TYPE_VALUES:
        return cast(UpdateIncidentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_DATA_TYPE_VALUES!r}")
