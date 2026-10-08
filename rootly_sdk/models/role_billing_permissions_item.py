from typing import Literal

RoleBillingPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_BILLING_PERMISSIONS_ITEM_VALUES: set[RoleBillingPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_billing_permissions_item(value: str | None) -> RoleBillingPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_BILLING_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_BILLING_PERMISSIONS_ITEM_VALUES!r}")
