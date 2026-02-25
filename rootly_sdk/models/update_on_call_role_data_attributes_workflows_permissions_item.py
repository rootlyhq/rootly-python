from typing import Literal, cast

UpdateOnCallRoleDataAttributesWorkflowsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesWorkflowsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_workflows_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesWorkflowsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesWorkflowsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES!r}"
    )
