from typing import Literal, cast

NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType = Literal["all", "any"]

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES: set[
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType
] = {
    "all",
    "any",
}


def check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_condition_type(
    value: str | None,
) -> NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES:
        return cast(NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES!r}"
    )
