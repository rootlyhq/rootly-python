from typing import Literal, cast

UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType = Literal["all", "any"]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES: set[
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType
] = {
    "all",
    "any",
}


def check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_condition_type(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES:
        return cast(UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITION_TYPE_VALUES!r}"
    )
