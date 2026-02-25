from typing import Literal, cast

CreateServiceNowIncidentTaskParamsTaskType = Literal["create_service_now_incident"]

CREATE_SERVICE_NOW_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateServiceNowIncidentTaskParamsTaskType] = {
    "create_service_now_incident",
}


def check_create_service_now_incident_task_params_task_type(
    value: str | None,
) -> CreateServiceNowIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_SERVICE_NOW_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateServiceNowIncidentTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_SERVICE_NOW_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
