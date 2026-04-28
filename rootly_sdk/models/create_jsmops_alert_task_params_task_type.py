from typing import Literal, cast

CreateJsmopsAlertTaskParamsTaskType = Literal["create_jsmops_alert"]

CREATE_JSMOPS_ALERT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateJsmopsAlertTaskParamsTaskType] = {
    "create_jsmops_alert",
}


def check_create_jsmops_alert_task_params_task_type(value: str | None) -> CreateJsmopsAlertTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_JSMOPS_ALERT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateJsmopsAlertTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_JSMOPS_ALERT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
