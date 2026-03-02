from typing import Literal, cast

NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType = Literal["AlertField"]

NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType
] = {
    "AlertField",
}


def check_new_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_conditionable_type(
    value: str | None,
) -> NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType | None:
    if value is None:
        return None
    if (
        value
        in NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES
    ):
        return cast(NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
