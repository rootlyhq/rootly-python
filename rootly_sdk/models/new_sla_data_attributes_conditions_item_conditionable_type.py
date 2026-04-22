from typing import Literal, cast

NewSlaDataAttributesConditionsItemConditionableType = Literal[
    "SLAs::BuiltInFieldCondition", "SLAs::CustomFieldCondition"
]

NEW_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    NewSlaDataAttributesConditionsItemConditionableType
] = {
    "SLAs::BuiltInFieldCondition",
    "SLAs::CustomFieldCondition",
}


def check_new_sla_data_attributes_conditions_item_conditionable_type(
    value: str | None,
) -> NewSlaDataAttributesConditionsItemConditionableType | None:
    if value is None:
        return None
    if value in NEW_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(NewSlaDataAttributesConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_SLA_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
