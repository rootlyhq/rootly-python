from typing import Literal, cast

NewRoleDataAttributesBillingPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_BILLING_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesBillingPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_billing_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesBillingPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_BILLING_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesBillingPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_BILLING_PERMISSIONS_ITEM_VALUES!r}"
    )
