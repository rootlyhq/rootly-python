from typing import Literal, cast

RoleWorkflowsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_WORKFLOWS_PERMISSIONS_ITEM_VALUES: set[RoleWorkflowsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_workflows_permissions_item(value: str | None) -> RoleWorkflowsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_WORKFLOWS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleWorkflowsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_WORKFLOWS_PERMISSIONS_ITEM_VALUES!r}")
