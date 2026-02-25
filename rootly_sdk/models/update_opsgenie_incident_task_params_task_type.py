from typing import Literal, cast

UpdateOpsgenieIncidentTaskParamsTaskType = Literal["update_opsgenie_incident"]

UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateOpsgenieIncidentTaskParamsTaskType] = {
    "update_opsgenie_incident",
}


def check_update_opsgenie_incident_task_params_task_type(value: str | None) -> UpdateOpsgenieIncidentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateOpsgenieIncidentTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
