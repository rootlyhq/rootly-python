from typing import Literal, cast

WorkflowGroupKind = Literal["action_item", "alert", "incident", "post_mortem", "pulse", "simple"]

WORKFLOW_GROUP_KIND_VALUES: set[WorkflowGroupKind] = {
    "action_item",
    "alert",
    "incident",
    "post_mortem",
    "pulse",
    "simple",
}


def check_workflow_group_kind(value: str | None) -> WorkflowGroupKind | None:
    if value is None:
        return None
    if value in WORKFLOW_GROUP_KIND_VALUES:
        return cast(WorkflowGroupKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_GROUP_KIND_VALUES!r}")
