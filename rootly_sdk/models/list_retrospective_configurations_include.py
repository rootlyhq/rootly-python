from typing import Literal, cast

ListRetrospectiveConfigurationsInclude = Literal["groups", "incident_types", "severities"]

LIST_RETROSPECTIVE_CONFIGURATIONS_INCLUDE_VALUES: set[ListRetrospectiveConfigurationsInclude] = {
    "groups",
    "incident_types",
    "severities",
}


def check_list_retrospective_configurations_include(value: str | None) -> ListRetrospectiveConfigurationsInclude | None:
    if value is None:
        return None
    if value in LIST_RETROSPECTIVE_CONFIGURATIONS_INCLUDE_VALUES:
        return cast(ListRetrospectiveConfigurationsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RETROSPECTIVE_CONFIGURATIONS_INCLUDE_VALUES!r}")
