from typing import Literal, cast

ListEscalationPoliciesInclude = Literal["escalation_policy_levels", "escalation_policy_paths", "groups", "services"]

LIST_ESCALATION_POLICIES_INCLUDE_VALUES: set[ListEscalationPoliciesInclude] = {
    "escalation_policy_levels",
    "escalation_policy_paths",
    "groups",
    "services",
}


def check_list_escalation_policies_include(value: str | None) -> ListEscalationPoliciesInclude | None:
    if value is None:
        return None
    if value in LIST_ESCALATION_POLICIES_INCLUDE_VALUES:
        return cast(ListEscalationPoliciesInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ESCALATION_POLICIES_INCLUDE_VALUES!r}")
