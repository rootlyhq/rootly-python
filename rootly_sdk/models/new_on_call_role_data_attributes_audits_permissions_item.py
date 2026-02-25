from typing import Literal, cast

NewOnCallRoleDataAttributesAuditsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesAuditsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_audits_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesAuditsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesAuditsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_AUDITS_PERMISSIONS_ITEM_VALUES!r}"
    )
