from typing import Literal, cast

EscalationPathRuleServiceRuleType = Literal["service"]

ESCALATION_PATH_RULE_SERVICE_RULE_TYPE_VALUES: set[EscalationPathRuleServiceRuleType] = {
    "service",
}


def check_escalation_path_rule_service_rule_type(value: str | None) -> EscalationPathRuleServiceRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_SERVICE_RULE_TYPE_VALUES:
        return cast(EscalationPathRuleServiceRuleType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_SERVICE_RULE_TYPE_VALUES!r}")
