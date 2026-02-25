from typing import Literal, cast

UpdateAlertGroupDataAttributesConditionsItemConditionableType = Literal["AlertField"]

UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES: set[
    UpdateAlertGroupDataAttributesConditionsItemConditionableType
] = {
    "AlertField",
}


def check_update_alert_group_data_attributes_conditions_item_conditionable_type(
    value: str | None,
) -> UpdateAlertGroupDataAttributesConditionsItemConditionableType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES:
        return cast(UpdateAlertGroupDataAttributesConditionsItemConditionableType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_CONDITIONABLE_TYPE_VALUES!r}"
    )
