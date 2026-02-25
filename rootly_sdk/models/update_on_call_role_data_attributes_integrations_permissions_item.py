from typing import Literal, cast

UpdateOnCallRoleDataAttributesIntegrationsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesIntegrationsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_integrations_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesIntegrationsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesIntegrationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
