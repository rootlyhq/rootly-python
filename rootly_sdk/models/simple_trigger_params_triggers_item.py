from typing import Literal, cast

SimpleTriggerParamsTriggersItem = Literal["slack_command"]

SIMPLE_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES: set[SimpleTriggerParamsTriggersItem] = {
    "slack_command",
}


def check_simple_trigger_params_triggers_item(value: str | None) -> SimpleTriggerParamsTriggersItem | None:
    if value is None:
        return None
    if value in SIMPLE_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES:
        return cast(SimpleTriggerParamsTriggersItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SIMPLE_TRIGGER_PARAMS_TRIGGERS_ITEM_VALUES!r}")
