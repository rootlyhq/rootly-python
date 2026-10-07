from typing import Literal

UpdateProblemActionItemDataType = Literal["problem_action_items"]

UPDATE_PROBLEM_ACTION_ITEM_DATA_TYPE_VALUES: set[UpdateProblemActionItemDataType] = {
    "problem_action_items",
}


def check_update_problem_action_item_data_type(value: str | None) -> UpdateProblemActionItemDataType | None:
    if value is None:
        return None
    if value in UPDATE_PROBLEM_ACTION_ITEM_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_PROBLEM_ACTION_ITEM_DATA_TYPE_VALUES!r}")
