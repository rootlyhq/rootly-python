from typing import Literal, cast

NewRoleDataAttributesPulsesPermissionsItem = Literal["create", "read", "update"]

NEW_ROLE_DATA_ATTRIBUTES_PULSES_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesPulsesPermissionsItem] = {
    "create",
    "read",
    "update",
}


def check_new_role_data_attributes_pulses_permissions_item(
    value: str | None,
) -> NewRoleDataAttributesPulsesPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_PULSES_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesPulsesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_PULSES_PERMISSIONS_ITEM_VALUES!r}"
    )
