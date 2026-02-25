from typing import Literal, cast

NewAuthorizationDataAttributesPermissionsItem = Literal["authorize", "destroy", "read", "update"]

NEW_AUTHORIZATION_DATA_ATTRIBUTES_PERMISSIONS_ITEM_VALUES: set[NewAuthorizationDataAttributesPermissionsItem] = {
    "authorize",
    "destroy",
    "read",
    "update",
}


def check_new_authorization_data_attributes_permissions_item(
    value: str | None,
) -> NewAuthorizationDataAttributesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_AUTHORIZATION_DATA_ATTRIBUTES_PERMISSIONS_ITEM_VALUES:
        return cast(NewAuthorizationDataAttributesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_AUTHORIZATION_DATA_ATTRIBUTES_PERMISSIONS_ITEM_VALUES!r}"
    )
