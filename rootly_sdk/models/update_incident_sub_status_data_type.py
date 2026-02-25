from typing import Literal, cast

UpdateIncidentSubStatusDataType = Literal["incident_sub_statuses"]

UPDATE_INCIDENT_SUB_STATUS_DATA_TYPE_VALUES: set[UpdateIncidentSubStatusDataType] = {
    "incident_sub_statuses",
}


def check_update_incident_sub_status_data_type(value: str | None) -> UpdateIncidentSubStatusDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_SUB_STATUS_DATA_TYPE_VALUES:
        return cast(UpdateIncidentSubStatusDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_SUB_STATUS_DATA_TYPE_VALUES!r}")
