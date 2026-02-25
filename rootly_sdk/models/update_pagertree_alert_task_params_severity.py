from typing import Literal, cast

UpdatePagertreeAlertTaskParamsSeverity = Literal["auto", "SEV-1", "SEV-2", "SEV-3", "SEV-4"]

UPDATE_PAGERTREE_ALERT_TASK_PARAMS_SEVERITY_VALUES: set[UpdatePagertreeAlertTaskParamsSeverity] = {
    "auto",
    "SEV-1",
    "SEV-2",
    "SEV-3",
    "SEV-4",
}


def check_update_pagertree_alert_task_params_severity(value: str | None) -> UpdatePagertreeAlertTaskParamsSeverity | None:
    if value is None:
        return None
    if value in UPDATE_PAGERTREE_ALERT_TASK_PARAMS_SEVERITY_VALUES:
        return cast(UpdatePagertreeAlertTaskParamsSeverity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PAGERTREE_ALERT_TASK_PARAMS_SEVERITY_VALUES!r}"
    )
