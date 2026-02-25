from typing import Literal, cast

UpdateOnCallRoleDataAttributesWebhooksPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesWebhooksPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_webhooks_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesWebhooksPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesWebhooksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES!r}"
    )
