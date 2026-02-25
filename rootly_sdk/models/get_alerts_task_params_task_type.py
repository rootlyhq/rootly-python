from typing import Literal, cast

GetAlertsTaskParamsTaskType = Literal["get_alerts"]

GET_ALERTS_TASK_PARAMS_TASK_TYPE_VALUES: set[GetAlertsTaskParamsTaskType] = {
    "get_alerts",
}


def check_get_alerts_task_params_task_type(value: str | None) -> GetAlertsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in GET_ALERTS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(GetAlertsTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ALERTS_TASK_PARAMS_TASK_TYPE_VALUES!r}")
