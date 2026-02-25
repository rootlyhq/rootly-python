from typing import Literal, cast

NewIncidentDataType = Literal["incidents"]

NEW_INCIDENT_DATA_TYPE_VALUES: set[NewIncidentDataType] = {
    "incidents",
}


def check_new_incident_data_type(value: str | None) -> NewIncidentDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_DATA_TYPE_VALUES:
        return cast(NewIncidentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_DATA_TYPE_VALUES!r}")
