from typing import Literal

UpdateRoleDataAttributesSecretsPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_SECRETS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesSecretsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_secrets_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesSecretsPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_SECRETS_PERMISSIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_SECRETS_PERMISSIONS_ITEM_VALUES!r}"
    )
