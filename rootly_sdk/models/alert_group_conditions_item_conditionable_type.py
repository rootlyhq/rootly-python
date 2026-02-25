from typing import Literal, cast

AlertGroupConditionsItemConditionableType = Literal["AlertField"]

ALERT_GROUP_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[AlertGroupConditionsItemConditionableType] = {
    "AlertField",
}


def check_alert_group_conditions_item_conditionable_type(value: str | None) -> AlertGroupConditionsItemConditionableType | None:
    if value is None:
        return None
    if value in ALERT_GROUP_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(AlertGroupConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_GROUP_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
