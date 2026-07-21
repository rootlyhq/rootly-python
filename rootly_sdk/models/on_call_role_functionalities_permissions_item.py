from typing import Literal, cast

OnCallRoleFunctionalitiesPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES: set[OnCallRoleFunctionalitiesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_functionalities_permissions_item(
    value: str | None,
) -> OnCallRoleFunctionalitiesPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleFunctionalitiesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_FUNCTIONALITIES_PERMISSIONS_ITEM_VALUES!r}"
    )
