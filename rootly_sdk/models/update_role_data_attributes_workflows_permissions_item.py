from typing import Literal, cast

UpdateRoleDataAttributesWorkflowsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesWorkflowsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_workflows_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesWorkflowsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesWorkflowsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES!r}"
    )
