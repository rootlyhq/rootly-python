from typing import Literal, cast

UpdateRoleDataAttributesBillingPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_BILLING_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesBillingPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_billing_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesBillingPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_BILLING_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesBillingPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_BILLING_PERMISSIONS_ITEM_VALUES!r}"
    )
