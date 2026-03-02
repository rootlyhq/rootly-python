from typing import Literal, cast

UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType = Literal[
    "alert_field", "attribute", "payload"
]

UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType
] = {
    "alert_field",
    "attribute",
    "payload",
}


def check_update_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_type(
    value: str | None,
) -> UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES
    ):
        return cast(UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
