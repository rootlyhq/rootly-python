from typing import Literal, cast

UpdateAlertRetriggerRuleDataType = Literal["alert_retrigger_rules"]

UPDATE_ALERT_RETRIGGER_RULE_DATA_TYPE_VALUES: set[UpdateAlertRetriggerRuleDataType] = {
    "alert_retrigger_rules",
}


def check_update_alert_retrigger_rule_data_type(value: str | None) -> UpdateAlertRetriggerRuleDataType | None:
    if value is None:
        return None
    if value in UPDATE_ALERT_RETRIGGER_RULE_DATA_TYPE_VALUES:
        return cast(UpdateAlertRetriggerRuleDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_ALERT_RETRIGGER_RULE_DATA_TYPE_VALUES!r}")
