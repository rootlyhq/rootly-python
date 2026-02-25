from typing import Literal, cast

UpdateActionItemTaskParamsTaskType = Literal["update_action_item"]

UPDATE_ACTION_ITEM_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateActionItemTaskParamsTaskType] = {
    "update_action_item",
}


def check_update_action_item_task_params_task_type(value: str | None) -> UpdateActionItemTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_ACTION_ITEM_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateActionItemTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ACTION_ITEM_TASK_PARAMS_TASK_TYPE_VALUES!r}")
