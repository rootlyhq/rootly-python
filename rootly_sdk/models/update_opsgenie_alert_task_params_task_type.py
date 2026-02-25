from typing import Literal, cast

UpdateOpsgenieAlertTaskParamsTaskType = Literal["update_opsgenie_alert"]

UPDATE_OPSGENIE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateOpsgenieAlertTaskParamsTaskType] = {
    "update_opsgenie_alert",
}


def check_update_opsgenie_alert_task_params_task_type(value: str | None) -> UpdateOpsgenieAlertTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_OPSGENIE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateOpsgenieAlertTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_OPSGENIE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
