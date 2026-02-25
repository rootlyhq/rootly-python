from typing import Literal, cast

UpdateOpsgenieIncidentTaskParamsPriority = Literal["auto", "P1", "P2", "P3", "P4", "P5"]

UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_PRIORITY_VALUES: set[UpdateOpsgenieIncidentTaskParamsPriority] = {
    "auto",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
}


def check_update_opsgenie_incident_task_params_priority(
    value: str | None,
) -> UpdateOpsgenieIncidentTaskParamsPriority | None:
    if value is None:
        return None
    if value in UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_PRIORITY_VALUES:
        return cast(UpdateOpsgenieIncidentTaskParamsPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_PRIORITY_VALUES!r}"
    )
