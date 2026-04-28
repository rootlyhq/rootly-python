from typing import Literal, cast

SlaConditionsItemConditionableType = Literal["SLAs::BuiltInFieldCondition", "SLAs::CustomFieldCondition"]

SLA_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[SlaConditionsItemConditionableType] = {
    "SLAs::BuiltInFieldCondition",
    "SLAs::CustomFieldCondition",
}


def check_sla_conditions_item_conditionable_type(value: str | None) -> SlaConditionsItemConditionableType | None:
    if value is None:
        return None
    if value in SLA_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(SlaConditionsItemConditionableType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SLA_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}")
