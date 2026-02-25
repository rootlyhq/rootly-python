from typing import Literal, cast

OnCallRoleWorkflowsPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_WORKFLOWS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleWorkflowsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_workflows_permissions_item(value: str | None) -> OnCallRoleWorkflowsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_WORKFLOWS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleWorkflowsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_WORKFLOWS_PERMISSIONS_ITEM_VALUES!r}")
