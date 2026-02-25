from typing import Literal, cast

AlertTriggerParamsAlertPayloadConditionsLogic = Literal["ALL", "ANY", "NONE"]

ALERT_TRIGGER_PARAMS_ALERT_PAYLOAD_CONDITIONS_LOGIC_VALUES: set[AlertTriggerParamsAlertPayloadConditionsLogic] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_alert_trigger_params_alert_payload_conditions_logic(
    value: str | None,
) -> AlertTriggerParamsAlertPayloadConditionsLogic | None:
    if value is None:
        return None
    if value in ALERT_TRIGGER_PARAMS_ALERT_PAYLOAD_CONDITIONS_LOGIC_VALUES:
        return cast(AlertTriggerParamsAlertPayloadConditionsLogic, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_TRIGGER_PARAMS_ALERT_PAYLOAD_CONDITIONS_LOGIC_VALUES!r}"
    )
