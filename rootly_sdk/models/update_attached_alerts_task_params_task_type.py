from typing import Literal, cast

UpdateAttachedAlertsTaskParamsTaskType = Literal["update_attached_alerts"]

UPDATE_ATTACHED_ALERTS_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateAttachedAlertsTaskParamsTaskType] = {
    "update_attached_alerts",
}


def check_update_attached_alerts_task_params_task_type(
    value: str | None,
) -> UpdateAttachedAlertsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_ATTACHED_ALERTS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateAttachedAlertsTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ATTACHED_ALERTS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
