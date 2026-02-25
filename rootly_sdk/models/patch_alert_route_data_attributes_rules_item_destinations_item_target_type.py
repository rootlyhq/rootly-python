from typing import Literal, cast

PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType = Literal["EscalationPolicy", "Group", "Service"]

PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES: set[
    PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType
] = {
    "EscalationPolicy",
    "Group",
    "Service",
}


def check_patch_alert_route_data_attributes_rules_item_destinations_item_target_type(
    value: str | None,
) -> PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType | None:
    if value is None:
        return None
    if value in PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES:
        return cast(PatchAlertRouteDataAttributesRulesItemDestinationsItemTargetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_DESTINATIONS_ITEM_TARGET_TYPE_VALUES!r}"
    )
