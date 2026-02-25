from typing import Literal, cast

ListPlaybooksInclude = Literal[
    "causes", "environments", "functionalities", "groups", "incident_types", "services", "severities"
]

LIST_PLAYBOOKS_INCLUDE_VALUES: set[ListPlaybooksInclude] = {
    "causes",
    "environments",
    "functionalities",
    "groups",
    "incident_types",
    "services",
    "severities",
}


def check_list_playbooks_include(value: str | None) -> ListPlaybooksInclude | None:
    if value is None:
        return None
    if value in LIST_PLAYBOOKS_INCLUDE_VALUES:
        return cast(ListPlaybooksInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PLAYBOOKS_INCLUDE_VALUES!r}")
