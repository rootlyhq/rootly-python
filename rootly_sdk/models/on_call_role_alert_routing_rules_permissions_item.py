from typing import Literal, cast

OnCallRoleAlertRoutingRulesPermissionsItem = Literal["create", "delete", "read", "update"]

ON_CALL_ROLE_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES: set[OnCallRoleAlertRoutingRulesPermissionsItem] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_on_call_role_alert_routing_rules_permissions_item(value: str | None) -> OnCallRoleAlertRoutingRulesPermissionsItem | None:
    if value is None:
        return None
    if value in ON_CALL_ROLE_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES:
        return cast(OnCallRoleAlertRoutingRulesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ON_CALL_ROLE_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES!r}"
    )
