from typing import Literal, cast

UpdateOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem = Literal["create", "delete", "read", "update"]

UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES: set[
    UpdateOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_update_on_call_role_data_attributes_alert_routing_rules_permissions_item(
    value: str | None,
) -> UpdateOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem | None:
    if value is None:
        return None
    if value in UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES:
        return cast(UpdateOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES!r}"
    )
