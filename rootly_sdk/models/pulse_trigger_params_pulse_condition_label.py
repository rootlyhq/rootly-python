from typing import Literal, cast

PulseTriggerParamsPulseConditionLabel = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

PULSE_TRIGGER_PARAMS_PULSE_CONDITION_LABEL_VALUES: set[PulseTriggerParamsPulseConditionLabel] = {
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


def check_pulse_trigger_params_pulse_condition_label(value: str | None) -> PulseTriggerParamsPulseConditionLabel | None:
    if value is None:
        return None
    if value in PULSE_TRIGGER_PARAMS_PULSE_CONDITION_LABEL_VALUES:
        return cast(PulseTriggerParamsPulseConditionLabel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PULSE_TRIGGER_PARAMS_PULSE_CONDITION_LABEL_VALUES!r}"
    )
