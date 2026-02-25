from typing import Literal, cast

NewRoleDataAttributesIncidentsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_INCIDENTS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesIncidentsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_incidents_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesIncidentsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_INCIDENTS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesIncidentsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_INCIDENTS_PERMISSIONS_ITEM_VALUES!r}"
    )
