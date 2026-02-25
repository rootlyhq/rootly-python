from typing import Literal, cast

NewOnCallRoleDataAttributesWorkflowsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesWorkflowsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_workflows_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesWorkflowsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesWorkflowsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES!r}"
    )
