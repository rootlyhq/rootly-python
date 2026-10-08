from typing import Literal

EscalationPathRuleAlertUrgencyOperator = Literal["is", "is_not", "is_not_one_of", "is_one_of"]

ESCALATION_PATH_RULE_ALERT_URGENCY_OPERATOR_VALUES: set[EscalationPathRuleAlertUrgencyOperator] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_path_rule_alert_urgency_operator(
    value: str | None,
) -> EscalationPathRuleAlertUrgencyOperator | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_ALERT_URGENCY_OPERATOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_ALERT_URGENCY_OPERATOR_VALUES!r}"
    )
