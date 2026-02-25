from typing import Literal, cast

IncidentResponseDataType = Literal["incidents"]

INCIDENT_RESPONSE_DATA_TYPE_VALUES: set[IncidentResponseDataType] = {
    "incidents",
}


def check_incident_response_data_type(value: str | None) -> IncidentResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_RESPONSE_DATA_TYPE_VALUES!r}")
