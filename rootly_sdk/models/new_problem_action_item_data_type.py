from typing import Literal

NewProblemActionItemDataType = Literal["problem_action_items"]

NEW_PROBLEM_ACTION_ITEM_DATA_TYPE_VALUES: set[NewProblemActionItemDataType] = {
    "problem_action_items",
}


def check_new_problem_action_item_data_type(value: str | None) -> NewProblemActionItemDataType | None:
    if value is None:
        return None
    if value in NEW_PROBLEM_ACTION_ITEM_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_PROBLEM_ACTION_ITEM_DATA_TYPE_VALUES!r}")
