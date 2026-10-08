from typing import Literal

GetEscalationPathInclude = Literal["escalation_policy_levels"]

GET_ESCALATION_PATH_INCLUDE_VALUES: set[GetEscalationPathInclude] = {
    "escalation_policy_levels",
}


def check_get_escalation_path_include(value: str | None) -> GetEscalationPathInclude | None:
    if value is None:
        return None
    if value in GET_ESCALATION_PATH_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ESCALATION_PATH_INCLUDE_VALUES!r}")
