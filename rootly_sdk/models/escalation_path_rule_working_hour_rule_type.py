from typing import Literal, cast

EscalationPathRuleWorkingHourRuleType = Literal["working_hour"]

ESCALATION_PATH_RULE_WORKING_HOUR_RULE_TYPE_VALUES: set[EscalationPathRuleWorkingHourRuleType] = {
    "working_hour",
}


def check_escalation_path_rule_working_hour_rule_type(
    value: str | None,
) -> EscalationPathRuleWorkingHourRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_WORKING_HOUR_RULE_TYPE_VALUES:
        return cast(EscalationPathRuleWorkingHourRuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_WORKING_HOUR_RULE_TYPE_VALUES!r}"
    )
