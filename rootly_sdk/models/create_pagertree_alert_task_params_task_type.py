from typing import Literal, cast

CreatePagertreeAlertTaskParamsTaskType = Literal["create_pagertree_alert"]

CREATE_PAGERTREE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreatePagertreeAlertTaskParamsTaskType] = {
    "create_pagertree_alert",
}


def check_create_pagertree_alert_task_params_task_type(
    value: str | None,
) -> CreatePagertreeAlertTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_PAGERTREE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreatePagertreeAlertTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PAGERTREE_ALERT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
