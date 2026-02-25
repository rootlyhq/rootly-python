from typing import Literal, cast

RoleFormFieldsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_FORM_FIELDS_PERMISSIONS_ITEM_VALUES: set[RoleFormFieldsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_form_fields_permissions_item(value: str | None) -> RoleFormFieldsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_FORM_FIELDS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleFormFieldsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_FORM_FIELDS_PERMISSIONS_ITEM_VALUES!r}")
