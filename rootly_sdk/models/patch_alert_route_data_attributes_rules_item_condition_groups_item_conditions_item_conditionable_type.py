from typing import Literal, cast

PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType = Literal["AlertField"]

PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType
] = {
    "AlertField",
}


def check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_conditionable_type(
    value: str,
) -> PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType:
    if (
        value
        in PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES
    ):
        return cast(PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
