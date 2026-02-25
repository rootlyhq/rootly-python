from typing import Literal, cast

UpdateOpsgenieIncidentTaskParamsStatus = Literal["auto", "close", "open", "resolve"]

UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_STATUS_VALUES: set[UpdateOpsgenieIncidentTaskParamsStatus] = {
    "auto",
    "close",
    "open",
    "resolve",
}


def check_update_opsgenie_incident_task_params_status(value: str | None) -> UpdateOpsgenieIncidentTaskParamsStatus | None:
    if value is None:
        return None
    if value in UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_STATUS_VALUES:
        return cast(UpdateOpsgenieIncidentTaskParamsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_OPSGENIE_INCIDENT_TASK_PARAMS_STATUS_VALUES!r}"
    )
