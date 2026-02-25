from typing import Literal, cast

CreateOpsgenieAlertTaskParamsPriority = Literal["auto", "P1", "P2", "P3", "P4", "P5"]

CREATE_OPSGENIE_ALERT_TASK_PARAMS_PRIORITY_VALUES: set[CreateOpsgenieAlertTaskParamsPriority] = {
    "auto",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
}


def check_create_opsgenie_alert_task_params_priority(value: str | None) -> CreateOpsgenieAlertTaskParamsPriority | None:
    if value is None:
        return None
    if value in CREATE_OPSGENIE_ALERT_TASK_PARAMS_PRIORITY_VALUES:
        return cast(CreateOpsgenieAlertTaskParamsPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_OPSGENIE_ALERT_TASK_PARAMS_PRIORITY_VALUES!r}"
    )
