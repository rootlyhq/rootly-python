from typing import Literal, cast

RoleFunctionalitiesPermissionsItem = Literal["create", "delete", "read", "update"]

ROLE_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES: set[RoleFunctionalitiesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_functionalities_permissions_item(value: str | None) -> RoleFunctionalitiesPermissionsItem | None:
    if value is None:
        return None
    if value in ROLE_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES:
        return cast(RoleFunctionalitiesPermissionsItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ROLE_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES!r}")
