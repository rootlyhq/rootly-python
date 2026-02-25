from typing import Literal, cast

ListEscalationPathsInclude = Literal["escalation_policy_levels"]

LIST_ESCALATION_PATHS_INCLUDE_VALUES: set[ListEscalationPathsInclude] = {
    "escalation_policy_levels",
}


def check_list_escalation_paths_include(value: str | None) -> ListEscalationPathsInclude | None:
    if value is None:
        return None
    if value in LIST_ESCALATION_PATHS_INCLUDE_VALUES:
        return cast(ListEscalationPathsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ESCALATION_PATHS_INCLUDE_VALUES!r}")
