from typing import Literal

ProblemActionItemListDataItemType = Literal["problem_action_items"]

PROBLEM_ACTION_ITEM_LIST_DATA_ITEM_TYPE_VALUES: set[ProblemActionItemListDataItemType] = {
    "problem_action_items",
}


def check_problem_action_item_list_data_item_type(value: str | None) -> ProblemActionItemListDataItemType | None:
    if value is None:
        return None
    if value in PROBLEM_ACTION_ITEM_LIST_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_ACTION_ITEM_LIST_DATA_ITEM_TYPE_VALUES!r}")
