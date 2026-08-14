from typing import Literal, cast

NewAlertRetriggerRuleDataAttributesTimeoutMinutes = Literal[
    10, 20, 30, 40, 50, 60, 90, 120, 180, 240, 300, 360, 720, 1440
]

NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_TIMEOUT_MINUTES_VALUES: set[
    NewAlertRetriggerRuleDataAttributesTimeoutMinutes
] = {
    10,
    20,
    30,
    40,
    50,
    60,
    90,
    120,
    180,
    240,
    300,
    360,
    720,
    1440,
}


def check_new_alert_retrigger_rule_data_attributes_timeout_minutes(
    value: int,
) -> NewAlertRetriggerRuleDataAttributesTimeoutMinutes:
    if value in NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_TIMEOUT_MINUTES_VALUES:
        return cast(NewAlertRetriggerRuleDataAttributesTimeoutMinutes, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_TIMEOUT_MINUTES_VALUES!r}"
    )
