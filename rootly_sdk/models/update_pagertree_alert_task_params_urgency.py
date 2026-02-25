from typing import Literal, cast

UpdatePagertreeAlertTaskParamsUrgency = Literal["auto", "critical", "high", "low", "medium"]

UPDATE_PAGERTREE_ALERT_TASK_PARAMS_URGENCY_VALUES: set[UpdatePagertreeAlertTaskParamsUrgency] = {
    "auto",
    "critical",
    "high",
    "low",
    "medium",
}


def check_update_pagertree_alert_task_params_urgency(value: str | None) -> UpdatePagertreeAlertTaskParamsUrgency | None:
    if value is None:
        return None
    if value in UPDATE_PAGERTREE_ALERT_TASK_PARAMS_URGENCY_VALUES:
        return cast(UpdatePagertreeAlertTaskParamsUrgency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PAGERTREE_ALERT_TASK_PARAMS_URGENCY_VALUES!r}"
    )
