from typing import Literal, cast

AddActionItemTaskParamsStatus = Literal["cancelled", "done", "in_progress", "open"]

ADD_ACTION_ITEM_TASK_PARAMS_STATUS_VALUES: set[AddActionItemTaskParamsStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_add_action_item_task_params_status(value: str | None) -> AddActionItemTaskParamsStatus | None:
    if value is None:
        return None
    if value in ADD_ACTION_ITEM_TASK_PARAMS_STATUS_VALUES:
        return cast(AddActionItemTaskParamsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ACTION_ITEM_TASK_PARAMS_STATUS_VALUES!r}")
