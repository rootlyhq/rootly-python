from typing import Literal, cast

UpdateAlertGroupDataAttributesConditionsItemPropertyFieldConditionType = Literal[
    "contains",
    "does_not_contain",
    "ends_with",
    "is_empty",
    "is_not_one_of",
    "is_one_of",
    "matches_existing_alert",
    "matches_regex",
    "starts_with",
]

UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES: set[
    UpdateAlertGroupDataAttributesConditionsItemPropertyFieldConditionType
] = {
    "contains",
    "does_not_contain",
    "ends_with",
    "is_empty",
    "is_not_one_of",
    "is_one_of",
    "matches_existing_alert",
    "matches_regex",
    "starts_with",
}


def check_update_alert_group_data_attributes_conditions_item_property_field_condition_type(
    value: str | None,
) -> UpdateAlertGroupDataAttributesConditionsItemPropertyFieldConditionType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES:
        return cast(UpdateAlertGroupDataAttributesConditionsItemPropertyFieldConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES!r}"
    )
