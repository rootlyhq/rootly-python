from typing import Literal, cast

GetRetrospectiveConfigurationInclude = Literal["groups", "incident_types", "severities"]

GET_RETROSPECTIVE_CONFIGURATION_INCLUDE_VALUES: set[GetRetrospectiveConfigurationInclude] = {
    "groups",
    "incident_types",
    "severities",
}


def check_get_retrospective_configuration_include(value: str | None) -> GetRetrospectiveConfigurationInclude | None:
    if value is None:
        return None
    if value in GET_RETROSPECTIVE_CONFIGURATION_INCLUDE_VALUES:
        return cast(GetRetrospectiveConfigurationInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RETROSPECTIVE_CONFIGURATION_INCLUDE_VALUES!r}")
