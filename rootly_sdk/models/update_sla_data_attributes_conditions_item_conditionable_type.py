from typing import Literal, cast

UpdateSlaDataAttributesConditionsItemConditionableType = Literal[
    "SLAs::BuiltInFieldCondition", "SLAs::CustomFieldCondition"
]

UPDATE_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    UpdateSlaDataAttributesConditionsItemConditionableType
] = {
    "SLAs::BuiltInFieldCondition",
    "SLAs::CustomFieldCondition",
}


def check_update_sla_data_attributes_conditions_item_conditionable_type(
    value: str | None,
) -> UpdateSlaDataAttributesConditionsItemConditionableType | None:
    if value is None:
        return None
    if value in UPDATE_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(UpdateSlaDataAttributesConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
