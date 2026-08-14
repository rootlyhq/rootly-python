from typing import Literal, cast

UpdateAlertRetriggerRuleDataAttributesConditionsItemOperator = Literal[
    "contains",
    "does_not_contain",
    "ends_with",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches_regex",
    "starts_with",
]

UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_OPERATOR_VALUES: set[
    UpdateAlertRetriggerRuleDataAttributesConditionsItemOperator
] = {
    "contains",
    "does_not_contain",
    "ends_with",
    "is_not_one_of",
    "is_not_set",
    "is_one_of",
    "is_set",
    "matches_regex",
    "starts_with",
}


def check_update_alert_retrigger_rule_data_attributes_conditions_item_operator(
    value: str | None,
) -> UpdateAlertRetriggerRuleDataAttributesConditionsItemOperator | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_OPERATOR_VALUES:
        return cast(UpdateAlertRetriggerRuleDataAttributesConditionsItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_CONDITIONS_ITEM_OPERATOR_VALUES!r}"
    )
