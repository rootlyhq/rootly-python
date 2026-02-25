from typing import Literal, cast

UpdateAuthorizationDataAttributesPermissionsItem = Literal["authorize", "destroy", "read", "update"]

UPDATE_AUTHORIZATION_DATA_ATTRIBUTES_PERMISSIONS_ITEM_VALUES: set[UpdateAuthorizationDataAttributesPermissionsItem] = {
    "authorize",
    "destroy",
    "read",
    "update",
}


def check_update_authorization_data_attributes_permissions_item(
    value: str | None,
) -> UpdateAuthorizationDataAttributesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_AUTHORIZATION_DATA_ATTRIBUTES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateAuthorizationDataAttributesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_AUTHORIZATION_DATA_ATTRIBUTES_PERMISSIONS_ITEM_VALUES!r}"
    )
