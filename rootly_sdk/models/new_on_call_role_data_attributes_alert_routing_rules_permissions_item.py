from typing import Literal, cast

NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem = Literal["create", "delete", "read", "update"]

NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES: set[
    NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem
] = {
    "create",
    "delete",
    "read",
    "update",
}


def check_new_on_call_role_data_attributes_alert_routing_rules_permissions_item(
    value: str,
) -> NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem:
    if value in NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES:
        return cast(NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ON_CALL_ROLE_DATA_ATTRIBUTES_ALERT_ROUTING_RULES_PERMISSIONS_ITEM_VALUES!r}"
    )
