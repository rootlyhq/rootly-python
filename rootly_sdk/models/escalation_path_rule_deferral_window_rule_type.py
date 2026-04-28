from typing import Literal, cast

EscalationPathRuleDeferralWindowRuleType = Literal["deferral_window"]

ESCALATION_PATH_RULE_DEFERRAL_WINDOW_RULE_TYPE_VALUES: set[EscalationPathRuleDeferralWindowRuleType] = {
    "deferral_window",
}


def check_escalation_path_rule_deferral_window_rule_type(
    value: str | None,
) -> EscalationPathRuleDeferralWindowRuleType | None:
    if value is None:
        return None
    if value in ESCALATION_PATH_RULE_DEFERRAL_WINDOW_RULE_TYPE_VALUES:
        return cast(EscalationPathRuleDeferralWindowRuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ESCALATION_PATH_RULE_DEFERRAL_WINDOW_RULE_TYPE_VALUES!r}"
    )
