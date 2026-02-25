from typing import Literal, cast

NewRoleDataAttributesWebhooksPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesWebhooksPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_role_data_attributes_webhooks_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesWebhooksPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesWebhooksPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_WEBHOOKS_PERMISSIONS_ITEM_VALUES!r}"
    )
