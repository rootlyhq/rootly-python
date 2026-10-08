from typing import Literal

NewWorkflowGroupDataAttributesKind = Literal[
    "action_item", "alert", "incident", "post_mortem", "problem", "pulse", "simple"
]

NEW_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES: set[NewWorkflowGroupDataAttributesKind] = {
    "action_item",
    "alert",
    "incident",
    "post_mortem",
    "problem",
    "pulse",
    "simple",
}


def check_new_workflow_group_data_attributes_kind(value: str | None) -> NewWorkflowGroupDataAttributesKind | None:
    if value is None:
        return None
    if value in NEW_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES!r}")
