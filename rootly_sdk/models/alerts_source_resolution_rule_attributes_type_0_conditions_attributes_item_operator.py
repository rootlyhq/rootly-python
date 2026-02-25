from typing import Literal, cast

AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemOperator = Literal[
    "contains", "does_not_contain", "ends_with", "is", "is_not", "starts_with"
]

ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_OPERATOR_VALUES: set[
    AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemOperator
] = {
    "contains",
    "does_not_contain",
    "ends_with",
    "is",
    "is_not",
    "starts_with",
}


def check_alerts_source_resolution_rule_attributes_type_0_conditions_attributes_item_operator(
    value: str | None,
) -> AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemOperator | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_OPERATOR_VALUES:
        return cast(AlertsSourceResolutionRuleAttributesType0ConditionsAttributesItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_OPERATOR_VALUES!r}"
    )
