from typing import Literal, cast

UpdateAlertGroupDataAttributesConditionType = Literal["all", "any"]

UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES: set[UpdateAlertGroupDataAttributesConditionType] = {
    "all",
    "any",
}


def check_update_alert_group_data_attributes_condition_type(
    value: str | None,
) -> UpdateAlertGroupDataAttributesConditionType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES:
        return cast(UpdateAlertGroupDataAttributesConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES!r}"
    )
