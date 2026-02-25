from typing import Literal, cast

OnCallRoleWebhooksPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_WEBHOOKS_PERMISSIONS_ITEM_VALUES: set[OnCallRoleWebhooksPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_webhooks_permissions_item(value: str | None) -> OnCallRoleWebhooksPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_WEBHOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleWebhooksPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_WEBHOOKS_PERMISSIONS_ITEM_VALUES!r}")
