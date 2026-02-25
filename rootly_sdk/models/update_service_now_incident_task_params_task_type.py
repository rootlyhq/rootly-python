from typing import Literal, cast

UpdateServiceNowIncidentTaskParamsTaskType = Literal["update_service_now_incident"]

UPDATE_SERVICE_NOW_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateServiceNowIncidentTaskParamsTaskType] = {
    "update_service_now_incident",
}


def check_update_service_now_incident_task_params_task_type(value: str | None) -> UpdateServiceNowIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_SERVICE_NOW_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateServiceNowIncidentTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SERVICE_NOW_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
