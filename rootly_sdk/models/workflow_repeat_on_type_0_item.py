from typing import Literal, cast

WorkflowRepeatOnType0Item = Literal["F", "M", "R", "S", "T", "U", "W"]

WORKFLOW_REPEAT_ON_TYPE_0_ITEM_VALUES: set[WorkflowRepeatOnType0Item] = {
    "F",
    "M",
    "R",
    "S",
    "T",
    "U",
    "W",
}


def check_workflow_repeat_on_type_0_item(value: str | None) -> WorkflowRepeatOnType0Item | None:
    if value is None:
        return None
    if value in WORKFLOW_REPEAT_ON_TYPE_0_ITEM_VALUES:
        return cast(WorkflowRepeatOnType0Item, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_REPEAT_ON_TYPE_0_ITEM_VALUES!r}")
