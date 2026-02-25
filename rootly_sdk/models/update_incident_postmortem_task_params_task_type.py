from typing import Literal, cast

UpdateIncidentPostmortemTaskParamsTaskType = Literal["update_incident_postmortem"]

UPDATE_INCIDENT_POSTMORTEM_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateIncidentPostmortemTaskParamsTaskType] = {
    "update_incident_postmortem",
}


def check_update_incident_postmortem_task_params_task_type(value: str | None) -> UpdateIncidentPostmortemTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_POSTMORTEM_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateIncidentPostmortemTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_POSTMORTEM_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
