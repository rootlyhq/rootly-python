from typing import Literal, cast

UpdateIncidentStatusTimestampTaskParamsTaskType = Literal["update_status"]

UPDATE_INCIDENT_STATUS_TIMESTAMP_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateIncidentStatusTimestampTaskParamsTaskType] = {
    "update_status",
}


def check_update_incident_status_timestamp_task_params_task_type(
    value: str | None,
) -> UpdateIncidentStatusTimestampTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_STATUS_TIMESTAMP_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateIncidentStatusTimestampTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_STATUS_TIMESTAMP_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
