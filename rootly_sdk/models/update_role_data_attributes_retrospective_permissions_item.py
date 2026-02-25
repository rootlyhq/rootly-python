from typing import Literal, cast

UpdateRoleDataAttributesRetrospectivePermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesRetrospectivePermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_retrospective_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesRetrospectivePermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesRetrospectivePermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES!r}"
    )
