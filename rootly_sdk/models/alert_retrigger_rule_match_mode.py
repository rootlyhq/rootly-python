from typing import Literal, cast

AlertRetriggerRuleMatchMode = Literal["match-all-rules", "match-any-rule"]

ALERT_RETRIGGER_RULE_MATCH_MODE_VALUES: set[AlertRetriggerRuleMatchMode] = {
    "match-all-rules",
    "match-any-rule",
}


def check_alert_retrigger_rule_match_mode(value: str | None) -> AlertRetriggerRuleMatchMode | None:
    if value is None:
        return None
    if value in ALERT_RETRIGGER_RULE_MATCH_MODE_VALUES:
        return cast(AlertRetriggerRuleMatchMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_RETRIGGER_RULE_MATCH_MODE_VALUES!r}")
