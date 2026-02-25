from typing import Literal, cast

CreatePagertreeAlertTaskParamsSeverity = Literal["auto", "SEV-1", "SEV-2", "SEV-3", "SEV-4"]

CREATE_PAGERTREE_ALERT_TASK_PARAMS_SEVERITY_VALUES: set[CreatePagertreeAlertTaskParamsSeverity] = {
    "auto",
    "SEV-1",
    "SEV-2",
    "SEV-3",
    "SEV-4",
}


def check_create_pagertree_alert_task_params_severity(
    value: str | None,
) -> CreatePagertreeAlertTaskParamsSeverity | None:
    if value is None:
        return None
    if value in CREATE_PAGERTREE_ALERT_TASK_PARAMS_SEVERITY_VALUES:
        return cast(CreatePagertreeAlertTaskParamsSeverity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PAGERTREE_ALERT_TASK_PARAMS_SEVERITY_VALUES!r}"
    )
