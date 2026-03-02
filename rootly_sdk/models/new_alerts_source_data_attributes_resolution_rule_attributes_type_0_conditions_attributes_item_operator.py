from typing import Literal, cast

NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator = Literal[
    "contains", "does_not_contain", "ends_with", "is", "is_not", "starts_with"
]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_OPERATOR_VALUES: set[
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator
] = {
    "contains",
    "does_not_contain",
    "ends_with",
    "is",
    "is_not",
    "starts_with",
}


def check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_operator(
    value: str | None,
) -> NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator | None:
    if value is None:
        return None
    if (
        value
        in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_OPERATOR_VALUES
    ):
        return cast(NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_OPERATOR_VALUES!r}"
    )
