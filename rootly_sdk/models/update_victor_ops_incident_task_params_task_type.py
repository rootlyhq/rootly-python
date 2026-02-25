from typing import Literal, cast

UpdateVictorOpsIncidentTaskParamsTaskType = Literal["update_victor_ops_incident"]

UPDATE_VICTOR_OPS_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateVictorOpsIncidentTaskParamsTaskType] = {
    "update_victor_ops_incident",
}


def check_update_victor_ops_incident_task_params_task_type(value: str | None) -> UpdateVictorOpsIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_VICTOR_OPS_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateVictorOpsIncidentTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_VICTOR_OPS_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
