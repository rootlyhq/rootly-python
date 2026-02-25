from typing import Literal, cast

GetPlaybookInclude = Literal[
    "causes", "environments", "functionalities", "groups", "incident_types", "services", "severities"
]

GET_PLAYBOOK_INCLUDE_VALUES: set[GetPlaybookInclude] = {
    "causes",
    "environments",
    "functionalities",
    "groups",
    "incident_types",
    "services",
    "severities",
}


def check_get_playbook_include(value: str | None) -> GetPlaybookInclude | None:
    if value is None:
        return None
    if value in GET_PLAYBOOK_INCLUDE_VALUES:
        return cast(GetPlaybookInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PLAYBOOK_INCLUDE_VALUES!r}")
