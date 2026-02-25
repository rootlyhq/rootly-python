from typing import Literal, cast

NewOnCallRoleDataAttributesContactsPermissionsItem = Literal["read"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_CONTACTS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesContactsPermissionsItem
] = {
    "read",
}


def check_new_on_call_role_data_attributes_contacts_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesContactsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_CONTACTS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesContactsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_CONTACTS_PERMISSIONS_ITEM_VALUES!r}"
    )
