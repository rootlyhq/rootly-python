from typing import Literal, cast

NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType = Literal["attribute", "payload"]

NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType
] = {
    "attribute",
    "payload",
}


def check_new_alert_routing_rule_data_attributes_conditions_item_property_field_type(
    value: str | None,
) -> NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
