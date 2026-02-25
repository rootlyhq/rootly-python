from typing import Literal, cast

NewRoleDataAttributesPlaybooksPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_PLAYBOOKS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesPlaybooksPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_playbooks_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesPlaybooksPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_PLAYBOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesPlaybooksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_PLAYBOOKS_PERMISSIONS_ITEM_VALUES!r}"
    )
