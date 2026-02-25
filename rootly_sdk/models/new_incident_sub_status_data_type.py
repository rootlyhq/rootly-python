from typing import Literal, cast

NewIncidentSubStatusDataType = Literal["incident_sub_statuses"]

NEW_INCIDENT_SUB_STATUS_DATA_TYPE_VALUES: set[NewIncidentSubStatusDataType] = {
    "incident_sub_statuses",
}


def check_new_incident_sub_status_data_type(value: str | None) -> NewIncidentSubStatusDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_SUB_STATUS_DATA_TYPE_VALUES:
        return cast(NewIncidentSubStatusDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_SUB_STATUS_DATA_TYPE_VALUES!r}")
