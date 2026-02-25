from typing import Literal, cast

AlertTriggerParamsAlertCondition = Literal["ALL", "ANY", "NONE"]

ALERT_TRIGGER_PARAMS_ALERT_CONDITION_VALUES: set[AlertTriggerParamsAlertCondition] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_alert_trigger_params_alert_condition(value: str | None) -> AlertTriggerParamsAlertCondition | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_ALERT_CONDITION_VALUES:
        return cast(AlertTriggerParamsAlertCondition, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_ALERT_CONDITION_VALUES!r}")
