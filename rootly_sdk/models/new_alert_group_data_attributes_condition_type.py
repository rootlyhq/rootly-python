from typing import Literal, cast

NewAlertGroupDataAttributesConditionType = Literal["all", "any"]

NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES: set[NewAlertGroupDataAttributesConditionType] = {
    "all",
    "any",
}


def check_new_alert_group_data_attributes_condition_type(value: str | None) -> NewAlertGroupDataAttributesConditionType | None:
    if value is None:
        return None
    if value in NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES:
        return cast(NewAlertGroupDataAttributesConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITION_TYPE_VALUES!r}"
    )
