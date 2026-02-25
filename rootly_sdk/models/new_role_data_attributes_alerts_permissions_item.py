from typing import Literal, cast

NewRoleDataAttributesAlertsPermissionsItem = Literal["create", "read"]

NEW_ROLE_DATA_ATTRIBUTES_ALERTS_PERMISSIONS_ITEM_VALUES: set[NewRoleDataAttributesAlertsPermissionsItem] = {
    "create",
    "read",
}


def check_new_role_data_attributes_alerts_permissions_item(value: str | None) -> NewRoleDataAttributesAlertsPermissionsItem | None:
    if value is None:
        return None
    if value in NEW_ROLE_DATA_ATTRIBUTES_ALERTS_PERMISSIONS_ITEM_VALUES:
        return cast(NewRoleDataAttributesAlertsPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ROLE_DATA_ATTRIBUTES_ALERTS_PERMISSIONS_ITEM_VALUES!r}"
    )
