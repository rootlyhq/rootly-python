from typing import Literal

NewProblemActionItemDataAttributesPriority = Literal["high", "low", "medium"]

NEW_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES: set[NewProblemActionItemDataAttributesPriority] = {
    "high",
    "low",
    "medium",
}


def check_new_problem_action_item_data_attributes_priority(
    value: str | None,
) -> NewProblemActionItemDataAttributesPriority | None:
    if value is None:
        return None
    if value in NEW_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES!r}"
    )
