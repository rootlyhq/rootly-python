from typing import Literal, cast

AlertRouteRulesItemDestinationsItemTargetType = Literal["EscalationPolicy", "Group", "Service"]

ALERT_ROUTE_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES: set[AlertRouteRulesItemDestinationsItemTargetType] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_alert_route_rules_item_destinations_item_target_type(
    value: str | None,
) -> AlertRouteRulesItemDestinationsItemTargetType | None:
    if value is None:
        return None
    if value in ALERT_ROUTE_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES:
        return cast(AlertRouteRulesItemDestinationsItemTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_ROUTE_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES!r}"
    )
