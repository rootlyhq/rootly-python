from typing import Literal, cast

NewAlertGroupDataAttributesConditionsItemPropertyFieldConditionType = Literal[
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

NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES: set[
    NewAlertGroupDataAttributesConditionsItemPropertyFieldConditionType
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


def check_new_alert_group_data_attributes_conditions_item_property_field_condition_type(
    value: str | None,
) -> NewAlertGroupDataAttributesConditionsItemPropertyFieldConditionType | None:
    if value is None:
        return None
    if value in NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES:
        return cast(NewAlertGroupDataAttributesConditionsItemPropertyFieldConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_GROUP_DATA_ATTRIBUTES_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES!r}"
    )
