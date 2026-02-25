from typing import Literal, cast

UpdateOpsgenieAlertTaskParamsPriority = Literal["auto", "P1", "P2", "P3", "P4", "P5"]

UPDATE_OPSGENIE_ALERT_TASK_PARAMS_PRIORITY_VALUES: set[UpdateOpsgenieAlertTaskParamsPriority] = {
    "auto",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
}


def check_update_opsgenie_alert_task_params_priority(value: str | None) -> UpdateOpsgenieAlertTaskParamsPriority | None:
    if value is None:
        return None
    if value in UPDATE_OPSGENIE_ALERT_TASK_PARAMS_PRIORITY_VALUES:
        return cast(UpdateOpsgenieAlertTaskParamsPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_OPSGENIE_ALERT_TASK_PARAMS_PRIORITY_VALUES!r}"
    )
