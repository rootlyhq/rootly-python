from typing import Literal, cast

UpdateRoleDataAttributesSeveritiesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_SEVERITIES_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesSeveritiesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_severities_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesSeveritiesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_SEVERITIES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesSeveritiesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_SEVERITIES_PERMISSIONS_ITEM_VALUES!r}"
    )
