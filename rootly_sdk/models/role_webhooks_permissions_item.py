from typing import Literal, cast

RoleWebhooksPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_WEBHOOKS_PERMISSIONS_ITEM_VALUES: set[RoleWebhooksPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_webhooks_permissions_item(value: str | None) -> RoleWebhooksPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_WEBHOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(RoleWebhooksPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_WEBHOOKS_PERMISSIONS_ITEM_VALUES!r}")
