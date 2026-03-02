from typing import Literal, cast

UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType = Literal[
    "AlertField"
]

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType
] = {
    "AlertField",
}


def check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType | None:
    if value is None:
        return None
    if (
        value
        in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES
    ):
        return cast(
            UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType,
            value,
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_RESOLUTION_RULE_ATTRIBUTES_TYPE_0_CONDITIONS_ATTRIBUTES_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
