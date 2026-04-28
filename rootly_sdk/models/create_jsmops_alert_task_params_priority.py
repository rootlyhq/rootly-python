from typing import Literal, cast

CreateJsmopsAlertTaskParamsPriority = Literal["auto", "P1", "P2", "P3", "P4", "P5"]

CREATE_JSMOPS_ALERT_TASK_PARAMS_PRIORITY_VALUES: set[CreateJsmopsAlertTaskParamsPriority] = {
    "auto",
    "P1",
    "P2",
    "P3",
    "P4",
    "P5",
}


def check_create_jsmops_alert_task_params_priority(value: str | None) -> CreateJsmopsAlertTaskParamsPriority | None:
    if value is None:
        return None
    if value in CREATE_JSMOPS_ALERT_TASK_PARAMS_PRIORITY_VALUES:
        return cast(CreateJsmopsAlertTaskParamsPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_JSMOPS_ALERT_TASK_PARAMS_PRIORITY_VALUES!r}")
