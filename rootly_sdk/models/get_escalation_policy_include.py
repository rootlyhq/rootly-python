from typing import Literal, cast

GetEscalationPolicyInclude = Literal["escalation_policy_levels", "escalation_policy_paths", "groups", "services"]

GET_ESCALATION_POLICY_INCLUDE_VALUES: set[GetEscalationPolicyInclude] = {
    "escalation_policy_levels",
    "escalation_policy_paths",
    "groups",
    "services",
}


def check_get_escalation_policy_include(value: str | None) -> GetEscalationPolicyInclude | None:
    if value is None:
        return None
    if value in GET_ESCALATION_POLICY_INCLUDE_VALUES:
        return cast(GetEscalationPolicyInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ESCALATION_POLICY_INCLUDE_VALUES!r}")
