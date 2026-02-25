from typing import Literal, cast

UpdateRoleDataAttributesAuditsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesAuditsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_audits_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesAuditsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesAuditsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES!r}"
    )
