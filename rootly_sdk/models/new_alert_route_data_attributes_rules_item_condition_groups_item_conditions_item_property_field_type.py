from typing import Literal, cast

NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType = Literal[
    "alert_field", "attribute", "payload"
]

NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType
] = {
    "alert_field",
    "attribute",
    "payload",
}


def check_new_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_type(
    value: str | None,
) -> NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if (
        value
        in NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES
    ):
        return cast(NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
