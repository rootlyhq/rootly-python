from typing import Literal, cast

UpdateOnCallRoleDataAttributesServicesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesServicesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_services_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesServicesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesServicesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES!r}"
    )
