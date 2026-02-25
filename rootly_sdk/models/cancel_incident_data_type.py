from typing import Literal, cast

CancelIncidentDataType = Literal["incidents"]

CANCEL_INCIDENT_DATA_TYPE_VALUES: set[CancelIncidentDataType] = {
    "incidents",
}


def check_cancel_incident_data_type(value: str | None) -> CancelIncidentDataType | None:
    if value is None:
        return None
    if value in CANCEL_INCIDENT_DATA_TYPE_VALUES:
        return cast(CancelIncidentDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CANCEL_INCIDENT_DATA_TYPE_VALUES!r}")
