from typing import Literal, cast

UpdateRoleDataAttributesIntegrationsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES: set[
    UpdateRoleDataAttributesIntegrationsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_integrations_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesIntegrationsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesIntegrationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
