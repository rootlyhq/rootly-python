from typing import Literal, cast

NewAlertRouteDataAttributesRulesItemDestinationsItemTargetType = Literal["EscalationPolicy", "Group", "Service"]

NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES: set[
    NewAlertRouteDataAttributesRulesItemDestinationsItemTargetType
] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_new_alert_route_data_attributes_rules_item_destinations_item_target_type(
    value: str | None,
) -> NewAlertRouteDataAttributesRulesItemDestinationsItemTargetType | None:
    if value is None:
        return None
    if value in NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES:
        return cast(NewAlertRouteDataAttributesRulesItemDestinationsItemTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES!r}"
    )
