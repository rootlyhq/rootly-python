from typing import Literal, cast

UpdatePagertreeAlertTaskParamsTaskType = Literal["update_pagertree_alert"]

UPDATE_PAGERTREE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdatePagertreeAlertTaskParamsTaskType] = {
    "update_pagertree_alert",
}


def check_update_pagertree_alert_task_params_task_type(value: str | None) -> UpdatePagertreeAlertTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_PAGERTREE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdatePagertreeAlertTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PAGERTREE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
