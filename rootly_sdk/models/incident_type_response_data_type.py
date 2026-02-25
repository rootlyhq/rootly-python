from typing import Literal, cast

IncidentTypeResponseDataType = Literal["incident_types"]

INCIDENT_TYPE_RESPONSE_DATA_TYPE_VALUES: set[IncidentTypeResponseDataType] = {
    "incident_types",
}


def check_incident_type_response_data_type(value: str | None) -> IncidentTypeResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_TYPE_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentTypeResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_TYPE_RESPONSE_DATA_TYPE_VALUES!r}")
