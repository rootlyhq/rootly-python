from typing import Literal, cast

AlertTriggerParamsAlertConditionPayload = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

ALERT_TRIGGER_PARAMS_ALERT_CONDITION_PAYLOAD_VALUES: set[AlertTriggerParamsAlertConditionPayload] = {
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


def check_alert_trigger_params_alert_condition_payload(value: str | None) -> AlertTriggerParamsAlertConditionPayload | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_ALERT_CONDITION_PAYLOAD_VALUES:
        return cast(AlertTriggerParamsAlertConditionPayload, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_ALERT_CONDITION_PAYLOAD_VALUES!r}"
    )
