from typing import Literal, cast

NewRoleDataAttributesIntegrationsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesIntegrationsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_integrations_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesIntegrationsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesIntegrationsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_INTEGRATIONS_PERMISSIONS_ITEM_VALUES!r}"
    )
