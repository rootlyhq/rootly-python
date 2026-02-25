from typing import Literal, cast

AlertsSourceResolutionRuleAttributesType0ConditionType = Literal["all", "any"]

ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES: set[
    AlertsSourceResolutionRuleAttributesType0ConditionType
] = {
    "all",
    "any",
}


def check_alerts_source_resolution_rule_attributes_type_0_condition_type(
    value: str | None,
) -> AlertsSourceResolutionRuleAttributesType0ConditionType | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES:
        return cast(AlertsSourceResolutionRuleAttributesType0ConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES!r}"
    )
