from typing import Literal, cast

IncidentSubStatusResponseDataType = Literal["incident_sub_statuses"]

INCIDENT_SUB_STATUS_RESPONSE_DATA_TYPE_VALUES: set[IncidentSubStatusResponseDataType] = {
    "incident_sub_statuses",
}


def check_incident_sub_status_response_data_type(value: str | None) -> IncidentSubStatusResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_SUB_STATUS_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentSubStatusResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_SUB_STATUS_RESPONSE_DATA_TYPE_VALUES!r}")
