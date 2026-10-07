from typing import Literal

RoleStatusPageUpdatesPermissionsType0Item = Literal["create", "delete", "read", "update"]

ROLE_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES: set[RoleStatusPageUpdatesPermissionsType0Item] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_role_status_page_updates_permissions_type_0_item(
    value: str | None,
) -> RoleStatusPageUpdatesPermissionsType0Item | None:
    if value is None:
        return None
    if value in ROLE_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROLE_STATUS_PAGE_UPDATES_PERMISSIONS_TYPE_0_ITEM_VALUES!r}"
    )
