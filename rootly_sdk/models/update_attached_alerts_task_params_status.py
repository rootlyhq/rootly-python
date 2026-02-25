from typing import Literal, cast

UpdateAttachedAlertsTaskParamsStatus = Literal["acknowledged", "resolved"]

UPDATE_ATTACHED_ALERTS_TASK_PARAMS_STATUS_VALUES: set[UpdateAttachedAlertsTaskParamsStatus] = {
    "acknowledged",
    "resolved",
}


def check_update_attached_alerts_task_params_status(value: str | None) -> UpdateAttachedAlertsTaskParamsStatus | None:
    if value is None:
        return None
    if value in UPDATE_ATTACHED_ALERTS_TASK_PARAMS_STATUS_VALUES:
        return cast(UpdateAttachedAlertsTaskParamsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ATTACHED_ALERTS_TASK_PARAMS_STATUS_VALUES!r}")
