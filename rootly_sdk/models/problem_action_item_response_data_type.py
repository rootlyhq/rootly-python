from typing import Literal

ProblemActionItemResponseDataType = Literal["problem_action_items"]

PROBLEM_ACTION_ITEM_RESPONSE_DATA_TYPE_VALUES: set[ProblemActionItemResponseDataType] = {
    "problem_action_items",
}


def check_problem_action_item_response_data_type(value: str | None) -> ProblemActionItemResponseDataType | None:
    if value is None:
        return None
    if value in PROBLEM_ACTION_ITEM_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_ACTION_ITEM_RESPONSE_DATA_TYPE_VALUES!r}")
