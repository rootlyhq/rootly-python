from typing import Literal, cast

NewRoleDataAttributesEnvironmentsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_ENVIRONMENTS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesEnvironmentsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_environments_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesEnvironmentsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_ENVIRONMENTS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesEnvironmentsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_ENVIRONMENTS_PERMISSIONS_ITEM_VALUES!r}"
    )
