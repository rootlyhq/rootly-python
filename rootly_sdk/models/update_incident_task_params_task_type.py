from typing import Literal, cast

UpdateIncidentTaskParamsTaskType = Literal["update_incident"]

UPDATE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateIncidentTaskParamsTaskType] = {
    "update_incident",
}


def check_update_incident_task_params_task_type(value: str | None) -> UpdateIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateIncidentTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
