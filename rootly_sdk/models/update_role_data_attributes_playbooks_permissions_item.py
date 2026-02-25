from typing import Literal, cast

UpdateRoleDataAttributesPlaybooksPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_PLAYBOOKS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesPlaybooksPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_playbooks_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesPlaybooksPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_PLAYBOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesPlaybooksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_PLAYBOOKS_PERMISSIONS_ITEM_VALUES!r}"
    )
