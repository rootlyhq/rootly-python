from typing import Literal

UpdateProblemActionItemDataAttributesStatus = Literal["cancelled", "done", "in_progress", "open"]

UPDATE_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES: set[UpdateProblemActionItemDataAttributesStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_update_problem_action_item_data_attributes_status(
    value: str | None,
) -> UpdateProblemActionItemDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
