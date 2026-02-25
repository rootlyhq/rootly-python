from typing import Literal, cast

AlertTriggerParamsAlertConditionStatus = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ALERT_TRIGGER_PARAMS_ALERT_CONDITION_STATUS_VALUES: set[AlertTriggerParamsAlertConditionStatus] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_alert_trigger_params_alert_condition_status(value: str | None) -> AlertTriggerParamsAlertConditionStatus | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_ALERT_CONDITION_STATUS_VALUES:
        return cast(AlertTriggerParamsAlertConditionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_ALERT_CONDITION_STATUS_VALUES!r}"
    )
