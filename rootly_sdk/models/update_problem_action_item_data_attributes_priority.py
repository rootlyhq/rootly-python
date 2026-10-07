from typing import Literal

UpdateProblemActionItemDataAttributesPriority = Literal["high", "low", "medium"]

UPDATE_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES: set[UpdateProblemActionItemDataAttributesPriority] = {
    "high",
    "low",
    "medium",
}


def check_update_problem_action_item_data_attributes_priority(
    value: str | None,
) -> UpdateProblemActionItemDataAttributesPriority | None:
    if value is None:
        return None
    if value in UPDATE_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PROBLEM_ACTION_ITEM_DATA_ATTRIBUTES_PRIORITY_VALUES!r}"
    )
