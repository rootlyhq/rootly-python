from typing import Literal

ProblemListDataItemType = Literal["problems"]

PROBLEM_LIST_DATA_ITEM_TYPE_VALUES: set[ProblemListDataItemType] = {
    "problems",
}


def check_problem_list_data_item_type(value: str | None) -> ProblemListDataItemType | None:
    if value is None:
        return None
    if value in PROBLEM_LIST_DATA_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROBLEM_LIST_DATA_ITEM_TYPE_VALUES!r}")
