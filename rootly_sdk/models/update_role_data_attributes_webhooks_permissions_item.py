from typing import Literal, cast

UpdateRoleDataAttributesWebhooksPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES: set[UpdateRoleDataAttributesWebhooksPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_role_data_attributes_webhooks_permissions_item(
    value: str | None,
) -> UpdateRoleDataAttributesWebhooksPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateRoleDataAttributesWebhooksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES!r}"
    )
