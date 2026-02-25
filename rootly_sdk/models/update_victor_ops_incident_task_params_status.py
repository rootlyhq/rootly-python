from typing import Literal, cast

UpdateVictorOpsIncidentTaskParamsStatus = Literal["ack", "auto", "resolve"]

UPDATE_VICTOR_OPS_INCIDENT_TASK_PARAMS_STATUS_VALUES: set[UpdateVictorOpsIncidentTaskParamsStatus] = {
    "ack",
    "auto",
    "resolve",
}


def check_update_victor_ops_incident_task_params_status(value: str | None) -> UpdateVictorOpsIncidentTaskParamsStatus | None:
    if value is None:
        return None
    if value in UPDATE_VICTOR_OPS_INCIDENT_TASK_PARAMS_STATUS_VALUES:
        return cast(UpdateVictorOpsIncidentTaskParamsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_VICTOR_OPS_INCIDENT_TASK_PARAMS_STATUS_VALUES!r}"
    )
