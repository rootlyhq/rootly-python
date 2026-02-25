from typing import Literal, cast

AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemConditionableType = Literal["AlertField"]

ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemConditionableType
] = {
    "AlertField",
}


def check_alerts_source_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type(
    value: str | None,
) -> AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemConditionableType | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
