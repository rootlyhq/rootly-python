from typing import Literal, cast

NewRoleDataAttributesSlasPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_SLAS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesSlasPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_slas_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesSlasPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_SLAS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesSlasPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_SLAS_PERMISSIONS_ITEM_VALUES!r}"
    )
