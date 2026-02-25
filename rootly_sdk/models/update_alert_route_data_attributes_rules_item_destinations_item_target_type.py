from typing import Literal, cast

UpdateAlertRouteDataAttributesRulesItemDestinationsItemTargetType = Literal["EscalationPolicy", "Group", "Service"]

UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES: set[
    UpdateAlertRouteDataAttributesRulesItemDestinationsItemTargetType
] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_update_alert_route_data_attributes_rules_item_destinations_item_target_type(
    value: str | None,
) -> UpdateAlertRouteDataAttributesRulesItemDestinationsItemTargetType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES:
        return cast(UpdateAlertRouteDataAttributesRulesItemDestinationsItemTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES!r}"
    )
