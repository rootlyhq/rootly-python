from typing import Literal, cast

EscalationPathRuleAlertUrgencyRuleType = Literal["alert_urgency"]

ESCALATION_PATH_RULE_ALERT_URGENCY_RULE_TYPE_VALUES: set[EscalationPathRuleAlertUrgencyRuleType] = {
    "alert_urgency",
}


def check_escalation_path_rule_alert_urgency_rule_type(
    value: str | None,
) -> EscalationPathRuleAlertUrgencyRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_ALERT_URGENCY_RULE_TYPE_VALUES:
        return cast(EscalationPathRuleAlertUrgencyRuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_ALERT_URGENCY_RULE_TYPE_VALUES!r}"
    )
