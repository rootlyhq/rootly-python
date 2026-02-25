from typing import Literal, cast

NewRoleDataAttributesRetrospectivePermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES: set[
    NewRoleDataAttributesRetrospectivePermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_retrospective_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesRetrospectivePermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesRetrospectivePermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_RETROSPECTIVE_PERMISSIONS_ITEM_VALUES!r}"
    )
