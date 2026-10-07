from typing import Literal

NewRoleDataAttributesWorkflowsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesWorkflowsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_workflows_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesWorkflowsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_WORKFLOWS_PERMISSIONS_ITEM_VALUES!r}"
    )
