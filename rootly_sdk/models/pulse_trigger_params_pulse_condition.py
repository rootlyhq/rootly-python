from typing import Literal, cast

PulseTriggerParamsPulseCondition = Literal["ALL", "ANY", "NONE"]

PULSE_TRIGGER_PARAMS_PULSE_CONDITION_VALUES: set[PulseTriggerParamsPulseCondition] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_pulse_trigger_params_pulse_condition(value: str | None) -> PulseTriggerParamsPulseCondition | None:
    if value is None:
        return None
    if value in PULSE_TRIGGER_PARAMS_PULSE_CONDITION_VALUES:
        return cast(PulseTriggerParamsPulseCondition, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PULSE_TRIGGER_PARAMS_PULSE_CONDITION_VALUES!r}")
