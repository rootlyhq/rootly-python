from typing import Literal, cast

EscalationPolicyPathMatchMode = Literal["match-all-rules", "match-any-rule"]

ESCALATION_POLICY_PATH_MATCH_MODE_VALUES: set[EscalationPolicyPathMatchMode] = {
    "match-all-rules",
    "match-any-rule",
}


def check_escalation_policy_path_match_mode(value: str | None) -> EscalationPolicyPathMatchMode | None:
    if value is None:
        return None
    if value in ESCALATION_POLICY_PATH_MATCH_MODE_VALUES:
        return cast(EscalationPolicyPathMatchMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ESCALATION_POLICY_PATH_MATCH_MODE_VALUES!r}")
