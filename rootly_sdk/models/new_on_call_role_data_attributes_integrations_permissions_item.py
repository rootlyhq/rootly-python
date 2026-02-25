from typing import Literal, cast

NewOnCallRoleDataAttributesIntegrationsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesIntegrationsPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_integrations_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesIntegrationsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesIntegrationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
