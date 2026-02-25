from typing import Literal, cast

AddActionItemTaskParamsTaskType = Literal["add_action_item"]

ADD_ACTION_ITEM_TASK_PARAMS_TASK_TYPE_VALUES: set[AddActionItemTaskParamsTaskType] = {
    "add_action_item",
}


def check_add_action_item_task_params_task_type(value: str | None) -> AddActionItemTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ADD_ACTION_ITEM_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AddActionItemTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ACTION_ITEM_TASK_PARAMS_TASK_TYPE_VALUES!r}")
