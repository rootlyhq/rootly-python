from typing import Literal, cast

NewRoleDataAttributesSeveritiesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_SEVERITIES_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesSeveritiesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_severities_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesSeveritiesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_SEVERITIES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesSeveritiesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_SEVERITIES_PERMISSIONS_ITEM_VALUES!r}"
    )
