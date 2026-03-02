from typing import Literal, cast

UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType = Literal["AlertField"]

UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType
] = {
    "AlertField",
}


def check_update_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_conditionable_type(
    value: str | None,
) -> UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES
    ):
        return cast(UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
