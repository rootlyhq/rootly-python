from typing import Literal, cast

NewOnCallRoleDataAttributesServicesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesServicesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_services_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesServicesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesServicesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES!r}"
    )
