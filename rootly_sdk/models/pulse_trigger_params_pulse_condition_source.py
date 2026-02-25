from typing import Literal, cast

PulseTriggerParamsPulseConditionSource = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

PULSE_TRIGGER_PARAMS_PULSE_CONDITION_SOURCE_VALUES: set[PulseTriggerParamsPulseConditionSource] = {
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


def check_pulse_trigger_params_pulse_condition_source(
    value: str | None,
) -> PulseTriggerParamsPulseConditionSource | None:
    if value is None:
        return None
    if value in PULSE_TRIGGER_PARAMS_PULSE_CONDITION_SOURCE_VALUES:
        return cast(PulseTriggerParamsPulseConditionSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PULSE_TRIGGER_PARAMS_PULSE_CONDITION_SOURCE_VALUES!r}"
    )
