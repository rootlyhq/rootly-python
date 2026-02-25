from typing import Literal, cast

CreateIncidentTaskParamsTaskType = Literal["create_incident"]

CREATE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateIncidentTaskParamsTaskType] = {
    "create_incident",
}


def check_create_incident_task_params_task_type(value: str | None) -> CreateIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateIncidentTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
