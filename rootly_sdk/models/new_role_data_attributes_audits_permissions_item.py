from typing import Literal, cast

NewRoleDataAttributesAuditsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesAuditsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_audits_permissions_item(value: str | None) -> NewRoleDataAttributesAuditsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesAuditsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES!r}"
    )
