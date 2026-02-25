from typing import Literal, cast

PulseTriggerParamsTriggerType = Literal["pulse"]

PULSE_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES: set[PulseTriggerParamsTriggerType] = {
    "pulse",
}


def check_pulse_trigger_params_trigger_type(value: str | None) -> PulseTriggerParamsTriggerType | None:
    if value is None:
        return None
    if value in PULSE_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES:
        return cast(PulseTriggerParamsTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PULSE_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES!r}")
