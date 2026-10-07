from typing import Literal

UpdateWorkflowGroupDataAttributesKind = Literal[
    "action_item", "alert", "incident", "post_mortem", "problem", "pulse", "simple"
]

UPDATE_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateWorkflowGroupDataAttributesKind] = {
    "action_item",
    "alert",
    "incident",
    "post_mortem",
    "problem",
    "pulse",
    "simple",
}


def check_update_workflow_group_data_attributes_kind(value: str | None) -> UpdateWorkflowGroupDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
