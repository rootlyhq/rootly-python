from typing import Literal, cast

AlertGroupConditionsItemPropertyFieldConditionType = Literal[
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

ALERT_GROUP_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES: set[
    AlertGroupConditionsItemPropertyFieldConditionType
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


def check_alert_group_conditions_item_property_field_condition_type(
    value: str | None,
) -> AlertGroupConditionsItemPropertyFieldConditionType | None:
    if value is None:
        return None
    if value in ALERT_GROUP_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES:
        return cast(AlertGroupConditionsItemPropertyFieldConditionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_GROUP_CONDITIONS_ITEM_PROPERTY_FIELD_CONDITION_TYPE_VALUES!r}"
    )
