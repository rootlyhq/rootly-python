from typing import Literal, cast

GetIncidentInclude = Literal[
    "action_items",
    "alerts",
    "causes",
    "custom_field_selections",
    "environments",
    "events",
    "feedbacks",
    "functionalities",
    "groups",
    "incident_post_mortem",
    "incident_types",
    "roles",
    "services",
    "slack_messages",
    "sub_statuses",
    "subscribers",
]

GET_INCIDENT_INCLUDE_VALUES: set[GetIncidentInclude] = {
    "action_items",
    "alerts",
    "causes",
    "custom_field_selections",
    "environments",
    "events",
    "feedbacks",
    "functionalities",
    "groups",
    "incident_post_mortem",
    "incident_types",
    "roles",
    "services",
    "slack_messages",
    "sub_statuses",
    "subscribers",
}


def check_get_incident_include(value: str | None) -> GetIncidentInclude | None:
    if value is None:
        return None
    if value in GET_INCIDENT_INCLUDE_VALUES:
        return cast(GetIncidentInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INCIDENT_INCLUDE_VALUES!r}")
