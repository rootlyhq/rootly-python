from typing import Literal, cast

OnCallRoleContactsPermissionsItem = Literal["read"]

ON_CALL_ROLE_CONTACTS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleContactsPermissionsItem] = {
    "read",
}


def check_on_call_role_contacts_permissions_item(value: str | None) -> OnCallRoleContactsPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_CONTACTS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleContactsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_CONTACTS_PERMISSIONS_ITEM_VALUES!r}")
