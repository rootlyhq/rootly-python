from typing import Literal, cast

NewAlertGroupDataAttributesConditionsItemConditionableType = Literal["AlertField"]

NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    NewAlertGroupDataAttributesConditionsItemConditionableType
] = {
    "AlertField",
}


def check_new_alert_group_data_attributes_conditions_item_conditionable_type(
    value: str | None,
) -> NewAlertGroupDataAttributesConditionsItemConditionableType | None:
    if value is None:
        return None
    if value in NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(NewAlertGroupDataAttributesConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
