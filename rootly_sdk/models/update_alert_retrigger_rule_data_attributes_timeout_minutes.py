from typing import Literal, cast

UpdateAlertRetriggerRuleDataAttributesTimeoutMinutes = Literal[
    10, 20, 30, 40, 50, 60, 90, 120, 180, 240, 300, 360, 720, 1440
]

UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_TIMEOUT_MINUTES_VALUES: set[
    UpdateAlertRetriggerRuleDataAttributesTimeoutMinutes
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


def check_update_alert_retrigger_rule_data_attributes_timeout_minutes(
    value: int,
) -> UpdateAlertRetriggerRuleDataAttributesTimeoutMinutes:
    if value in UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_TIMEOUT_MINUTES_VALUES:
        return cast(UpdateAlertRetriggerRuleDataAttributesTimeoutMinutes, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_RETRIGGER_RULE_DATA_ATTRIBUTES_TIMEOUT_MINUTES_VALUES!r}"
    )
