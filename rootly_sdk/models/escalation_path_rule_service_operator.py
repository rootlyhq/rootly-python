from typing import Literal

EscalationPathRuleServiceOperator = Literal["is", "is_not", "is_not_one_of", "is_one_of"]

ESCALATION_PATH_RULE_SERVICE_OPERATOR_VALUES: set[EscalationPathRuleServiceOperator] = {
    "is",
    "is_not",
    "is_not_one_of",
    "is_one_of",
}


def check_escalation_path_rule_service_operator(value: str | None) -> EscalationPathRuleServiceOperator | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_SERVICE_OPERATOR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_SERVICE_OPERATOR_VALUES!r}")
