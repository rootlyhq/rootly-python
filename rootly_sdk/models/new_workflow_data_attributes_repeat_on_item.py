from typing import Literal, cast

NewWorkflowDataAttributesRepeatOnItem = Literal["F", "M", "R", "S", "T", "U", "W"]

NEW_WORKFLOW_DATA_ATTRIBUTES_REPEAT_ON_ITEM_VALUES: set[NewWorkflowDataAttributesRepeatOnItem] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_new_workflow_data_attributes_repeat_on_item(value: str | None) -> NewWorkflowDataAttributesRepeatOnItem | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_DATA_ATTRIBUTES_REPEAT_ON_ITEM_VALUES:
        return cast(NewWorkflowDataAttributesRepeatOnItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_DATA_ATTRIBUTES_REPEAT_ON_ITEM_VALUES!r}"
    )
