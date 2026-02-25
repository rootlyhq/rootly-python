from typing import Literal, cast

NewRoleDataAttributesSecretsPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_SECRETS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesSecretsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_secrets_permissions_item(value: str | None) -> NewRoleDataAttributesSecretsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_SECRETS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesSecretsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_SECRETS_PERMISSIONS_ITEM_VALUES!r}"
    )
