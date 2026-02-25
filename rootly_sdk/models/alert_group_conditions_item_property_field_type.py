from typing import Literal, cast

AlertGroupConditionsItemPropertyFieldType = Literal["alert_field", "attribute", "payload"]

ALERT_GROUP_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES: set[AlertGroupConditionsItemPropertyFieldType] = {
    "alert_field",
    "attribute",
    "payload",
}


def check_alert_group_conditions_item_property_field_type(value: str | None) -> AlertGroupConditionsItemPropertyFieldType | None:
    if value is None:
        return None
    if value in ALERT_GROUP_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES:
        return cast(AlertGroupConditionsItemPropertyFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_GROUP_CONDITIONS_ITEM_PROPERTY_FIELD_TYPE_VALUES!r}"
    )
