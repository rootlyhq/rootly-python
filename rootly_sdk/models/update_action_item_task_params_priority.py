from typing import Literal, cast

UpdateActionItemTaskParamsPriority = Literal["high", "low", "medium"]

UPDATE_ACTION_ITEM_TASK_PARAMS_PRIORITY_VALUES: set[UpdateActionItemTaskParamsPriority] = {
    "high",
    "low",
    "medium",
}


def check_update_action_item_task_params_priority(value: str | None) -> UpdateActionItemTaskParamsPriority | None:
    if value is None:
        return None
    if value in UPDATE_ACTION_ITEM_TASK_PARAMS_PRIORITY_VALUES:
        return cast(UpdateActionItemTaskParamsPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ACTION_ITEM_TASK_PARAMS_PRIORITY_VALUES!r}")
