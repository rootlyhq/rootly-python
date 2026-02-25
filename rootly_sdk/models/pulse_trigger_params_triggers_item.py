from typing import Literal, cast

PulseTriggerParamsTriggersItem = Literal["pulse_created"]

PULSE_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES: set[PulseTriggerParamsTriggersItem] = {
    "pulse_created",
}


def check_pulse_trigger_params_triggers_item(value: str | None) -> PulseTriggerParamsTriggersItem | None:
    if value is None:
        return None
    if value in PULSE_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES:
        return cast(PulseTriggerParamsTriggersItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PULSE_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES!r}")
