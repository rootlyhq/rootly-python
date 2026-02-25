from typing import Literal, cast

CreateIncidentPostmortemTaskParamsTaskType = Literal["create_incident_postmortem"]

CREATE_INCIDENT_POSTMORTEM_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateIncidentPostmortemTaskParamsTaskType] = {
    "create_incident_postmortem",
}


def check_create_incident_postmortem_task_params_task_type(value: str | None) -> CreateIncidentPostmortemTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_INCIDENT_POSTMORTEM_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateIncidentPostmortemTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INCIDENT_POSTMORTEM_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
