from typing import Literal, cast

NewAlertGroupDataAttributesConditionsItemPropertyFieldType = Literal["alert_field", "attribute", "payload"]

NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    NewAlertGroupDataAttributesConditionsItemPropertyFieldType
] = {
    "alert_field",
    "attribute",
    "payload",
}


def check_new_alert_group_data_attributes_conditions_item_property_field_type(
    value: str | None,
) -> NewAlertGroupDataAttributesConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(NewAlertGroupDataAttributesConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
