from typing import Literal, cast

AlertTriggerParamsAlertConditionUrgency = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ALERT_TRIGGER_PARAMS_ALERT_CONDITION_URGENCY_VALUES: set[AlertTriggerParamsAlertConditionUrgency] = {
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


def check_alert_trigger_params_alert_condition_urgency(
    value: str | None,
) -> AlertTriggerParamsAlertConditionUrgency | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_ALERT_CONDITION_URGENCY_VALUES:
        return cast(AlertTriggerParamsAlertConditionUrgency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_ALERT_CONDITION_URGENCY_VALUES!r}"
    )
