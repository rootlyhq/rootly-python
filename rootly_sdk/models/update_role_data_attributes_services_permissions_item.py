from typing import Literal, cast

UpdateRoleDataAttributesServicesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesServicesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_services_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesServicesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesServicesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_SERVICES_PERMISSIONS_ITEM_VALUES!r}"
    )
