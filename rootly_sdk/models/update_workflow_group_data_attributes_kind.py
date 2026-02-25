from typing import Literal, cast

UpdateWorkflowGroupDataAttributesKind = Literal["action_item", "alert", "incident", "post_mortem", "pulse", "simple"]

UPDATE_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES: set[UpdateWorkflowGroupDataAttributesKind] = {
    "action_item",
    "alert",
    "incident",
    "post_mortem",
    "pulse",
    "simple",
}


def check_update_workflow_group_data_attributes_kind(value: str | None) -> UpdateWorkflowGroupDataAttributesKind | None:
    if value is None:
        return None
    if value in UPDATE_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES:
        return cast(UpdateWorkflowGroupDataAttributesKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORKFLOW_GROUP_DATA_ATTRIBUTES_KIND_VALUES!r}"
    )
