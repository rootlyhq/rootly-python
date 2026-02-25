from typing import Literal, cast

AlertTriggerParamsTriggerType = Literal["alert"]

ALERT_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES: set[AlertTriggerParamsTriggerType] = {
    "alert",
}


def check_alert_trigger_params_trigger_type(value: str | None) -> AlertTriggerParamsTriggerType | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES:
        return cast(AlertTriggerParamsTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES!r}")
