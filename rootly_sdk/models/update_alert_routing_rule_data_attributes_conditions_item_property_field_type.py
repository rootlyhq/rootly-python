from typing import Literal, cast

UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType = Literal["attribute", "payload"]

UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType
] = {
    "attribute",
    "payload",
}


def check_update_alert_routing_rule_data_attributes_conditions_item_property_field_type(
    value: str | None,
) -> UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_ROUTING_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
