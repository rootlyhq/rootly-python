from typing import Literal, cast

UpdateOnCallRoleDataAttributesContactsPermissionsItem = Literal["read"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_CONTACTS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesContactsPermissionsItem
] = {
    "read",
}


def check_update_on_call_role_data_attributes_contacts_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesContactsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_CONTACTS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesContactsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_CONTACTS_PERMISSIONS_ITEM_VALUES!r}"
    )
