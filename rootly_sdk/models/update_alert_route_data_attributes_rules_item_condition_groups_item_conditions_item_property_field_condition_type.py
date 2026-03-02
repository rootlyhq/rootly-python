from typing import Literal, cast

UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType = Literal[
    "contains",
    "does_not_contain",
    "ends_with",
    "is_empty",
    "is_not_one_of",
    "is_one_of",
    "matches_regex",
    "starts_with",
]

UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES: set[
    UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType
] = {
    "contains",
    "does_not_contain",
    "ends_with",
    "is_empty",
    "is_not_one_of",
    "is_one_of",
    "matches_regex",
    "starts_with",
}


def check_update_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_condition_type(
    value: str | None,
) -> UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES
    ):
        return cast(
            UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES!r}"
    )
