from typing import Literal, cast

CreatePagertreeAlertTaskParamsUrgency = Literal["auto", "critical", "high", "low", "medium"]

CREATE_PAGERTREE_ALERT_TASK_PARAMS_URGENCY_VALUES: set[CreatePagertreeAlertTaskParamsUrgency] = {
    "auto",
    "critical",
    "high",
    "low",
    "medium",
}


def check_create_pagertree_alert_task_params_urgency(value: str | None) -> CreatePagertreeAlertTaskParamsUrgency | None:
    if value is None:
        return None
    if value in CREATE_PAGERTREE_ALERT_TASK_PARAMS_URGENCY_VALUES:
        return cast(CreatePagertreeAlertTaskParamsUrgency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PAGERTREE_ALERT_TASK_PARAMS_URGENCY_VALUES!r}"
    )
