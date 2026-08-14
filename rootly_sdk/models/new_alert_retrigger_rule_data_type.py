from typing import Literal, cast

NewAlertRetriggerRuleDataType = Literal["alert_retrigger_rules"]

NEW_ALERT_RETRIGGER_RULE_DATA_TYPE_VALUES: set[NewAlertRetriggerRuleDataType] = {
    "alert_retrigger_rules",
}


def check_new_alert_retrigger_rule_data_type(value: str | None) -> NewAlertRetriggerRuleDataType | None:
    if value is None:
        return None
    if value in NEW_ALERT_RETRIGGER_RULE_DATA_TYPE_VALUES:
        return cast(NewAlertRetriggerRuleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_ALERT_RETRIGGER_RULE_DATA_TYPE_VALUES!r}")
