from typing import Literal, cast

ListIncidentsInclude = Literal[
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

LIST_INCIDENTS_INCLUDE_VALUES: set[ListIncidentsInclude] = {
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


def check_list_incidents_include(value: str | None) -> ListIncidentsInclude | None:
    if value is None:
        return None
    if value in LIST_INCIDENTS_INCLUDE_VALUES:
        return cast(ListIncidentsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENTS_INCLUDE_VALUES!r}")
