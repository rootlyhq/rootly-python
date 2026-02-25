from typing import Literal, cast

CreateSubIncidentTaskParamsTaskType = Literal["create_sub_incident"]

CREATE_SUB_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateSubIncidentTaskParamsTaskType] = {
    "create_sub_incident",
}


def check_create_sub_incident_task_params_task_type(value: str | None) -> CreateSubIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_SUB_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateSubIncidentTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_SUB_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
