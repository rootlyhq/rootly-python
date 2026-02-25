from typing import Literal, cast

RoleSecretsPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_SECRETS_PERMISSIONS_ITEM_VALUES: set[RoleSecretsPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_secrets_permissions_item(value: str | None) -> RoleSecretsPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_SECRETS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleSecretsPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_SECRETS_PERMISSIONS_ITEM_VALUES!r}")
