from typing import Literal, cast

SimpleTriggerParamsTriggerType = Literal["simple"]

SIMPLE_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES: set[SimpleTriggerParamsTriggerType] = {
    "simple",
}


def check_simple_trigger_params_trigger_type(value: str | None) -> SimpleTriggerParamsTriggerType | None:
    if value is None:
        return None
    if value in SIMPLE_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES:
        return cast(SimpleTriggerParamsTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SIMPLE_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES!r}")
