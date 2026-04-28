from typing import Literal, cast

UpdateRoleDataAttributesSlasPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_SLAS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesSlasPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_slas_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesSlasPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_SLAS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesSlasPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_SLAS_PERMISSIONS_ITEM_VALUES!r}"
    )
