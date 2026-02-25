from typing import Literal, cast

AddActionItemTaskParamsPriority = Literal["high", "low", "medium"]

ADD_ACTION_ITEM_TASK_PARAMS_PRIORITY_VALUES: set[AddActionItemTaskParamsPriority] = {
    "high",
    "low",
    "medium",
}


def check_add_action_item_task_params_priority(value: str | None) -> AddActionItemTaskParamsPriority | None:
    if value is None:
        return None
    if value in ADD_ACTION_ITEM_TASK_PARAMS_PRIORITY_VALUES:
        return cast(AddActionItemTaskParamsPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ACTION_ITEM_TASK_PARAMS_PRIORITY_VALUES!r}")
