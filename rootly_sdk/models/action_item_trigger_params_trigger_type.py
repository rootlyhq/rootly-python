from typing import Literal, cast

ActionItemTriggerParamsTriggerType = Literal["action_item"]

ACTION_ITEM_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES: set[ActionItemTriggerParamsTriggerType] = {
    "action_item",
}


def check_action_item_trigger_params_trigger_type(value: str | None) -> ActionItemTriggerParamsTriggerType | None:
    if value is None:
        return None
    if value in ACTION_ITEM_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES:
        return cast(ActionItemTriggerParamsTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_ITEM_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES!r}")
