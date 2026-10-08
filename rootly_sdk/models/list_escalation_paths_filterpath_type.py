from typing import Literal

ListEscalationPathsFilterpathType = Literal["deferral", "escalation"]

LIST_ESCALATION_PATHS_FILTERPATH_TYPE_VALUES: set[ListEscalationPathsFilterpathType] = {
    "deferral",
    "escalation",
}


def check_list_escalation_paths_filterpath_type(value: str | None) -> ListEscalationPathsFilterpathType | None:
    if value is None:
        return None
    if value in LIST_ESCALATION_PATHS_FILTERPATH_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ESCALATION_PATHS_FILTERPATH_TYPE_VALUES!r}")
