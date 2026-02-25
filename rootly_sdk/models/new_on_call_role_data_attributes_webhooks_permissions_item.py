from typing import Literal, cast

NewOnCallRoleDataAttributesWebhooksPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesWebhooksPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_webhooks_permissions_item(
    value: str | None,
) -> NewOnCallRoleDataAttributesWebhooksPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesWebhooksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES!r}"
    )
