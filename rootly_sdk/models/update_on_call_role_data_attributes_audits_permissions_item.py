from typing import Literal, cast

UpdateOnCallRoleDataAttributesAuditsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesAuditsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_audits_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesAuditsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesAuditsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES!r}"
    )
