from typing import Literal, cast

PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType = Literal[
    "alert_field", "attribute", "payload"
]

PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType
] = {
    "alert_field",
    "attribute",
    "payload",
}


def check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_type(
    value: str,
) -> PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType:
    if (
        value
        in PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES
    ):
        return cast(PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCH_ALERT_ROUTE_DATA_ATTRIBUTES_RULES_ITEM_CONDITION_GROUPS_ITEM_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
