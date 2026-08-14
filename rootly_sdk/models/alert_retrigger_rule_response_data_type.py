from typing import Literal, cast

AlertRetriggerRuleResponseDataType = Literal["alert_retrigger_rules"]

ALERT_RETRIGGER_RULE_RESPONSE_DATA_TYPE_VALUES: set[AlertRetriggerRuleResponseDataType] = {
    "alert_retrigger_rules",
}


def check_alert_retrigger_rule_response_data_type(value: str | None) -> AlertRetriggerRuleResponseDataType | None:
    if value is None:
        return None
    if value in ALERT_RETRIGGER_RULE_RESPONSE_DATA_TYPE_VALUES:
        return cast(AlertRetriggerRuleResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_RETRIGGER_RULE_RESPONSE_DATA_TYPE_VALUES!r}")
