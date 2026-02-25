from typing import Literal, cast

RolePulsesPermissionsItem = Literal["create", "read", "update"]

ROLE_PULSES_PERMISSIONS_ITEM_VALUES: set[RolePulsesPermissionsItem] = {
    "create",
    "read",
    "update",
}


def check_role_pulses_permissions_item(value: str | None) -> RolePulsesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_PULSES_PERMISSIONS_ITEM_VALUES:
        return cast(RolePulsesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_PULSES_PERMISSIONS_ITEM_VALUES!r}")
