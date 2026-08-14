from typing import Literal, cast

AlertRetriggerRuleConditionsItemOperator = Literal[
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

ALERT_RETRIGGER_RULE_CONDITIONS_ITEM_OPERATOR_VALUES: set[AlertRetriggerRuleConditionsItemOperator] = {
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


def check_alert_retrigger_rule_conditions_item_operator(
    value: str | None,
) -> AlertRetriggerRuleConditionsItemOperator | None:
    if value is None:
        return None
    if value in ALERT_RETRIGGER_RULE_CONDITIONS_ITEM_OPERATOR_VALUES:
        return cast(AlertRetriggerRuleConditionsItemOperator, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RETRIGGER_RULE_CONDITIONS_ITEM_OPERATOR_VALUES!r}"
    )
