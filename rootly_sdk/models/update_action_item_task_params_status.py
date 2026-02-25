from typing import Literal, cast

UpdateActionItemTaskParamsStatus = Literal["cancelled", "done", "in_progress", "open"]

UPDATE_ACTION_ITEM_TASK_PARAMS_STATUS_VALUES: set[UpdateActionItemTaskParamsStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_update_action_item_task_params_status(value: str | None) -> UpdateActionItemTaskParamsStatus | None:
    if value is None:
        return None
    if value in UPDATE_ACTION_ITEM_TASK_PARAMS_STATUS_VALUES:
        return cast(UpdateActionItemTaskParamsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ACTION_ITEM_TASK_PARAMS_STATUS_VALUES!r}")
