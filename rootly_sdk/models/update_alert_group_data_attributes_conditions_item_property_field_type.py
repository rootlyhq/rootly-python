from typing import Literal, cast

UpdateAlertGroupDataAttributesConditionsItemPropertyFieldType = Literal["alert_field", "attribute", "payload"]

UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[
    UpdateAlertGroupDataAttributesConditionsItemPropertyFieldType
] = {
    "alert_field",
    "attribute",
    "payload",
}


def check_update_alert_group_data_attributes_conditions_item_property_field_type(
    value: str | None,
) -> UpdateAlertGroupDataAttributesConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(UpdateAlertGroupDataAttributesConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
