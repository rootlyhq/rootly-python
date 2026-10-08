from typing import Literal

NewProblemActionItemDataAttributesStatus = Literal["cancelled", "done", "in_progress", "open"]

NEW_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES: set[NewProblemActionItemDataAttributesStatus] = {
    "cancelled",
    "done",
    "in_progress",
    "open",
}


def check_new_problem_action_item_data_attributes_status(
    value: str | None,
) -> NewProblemActionItemDataAttributesStatus | None:
    if value is None:
        return None
    if value in NEW_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
