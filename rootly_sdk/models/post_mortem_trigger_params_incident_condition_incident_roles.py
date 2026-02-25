from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionIncidentRoles = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_ROLES_VALUES: set[
    PostMortemTriggerParamsIncidentConditionIncidentRoles
] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_incident_roles(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionIncidentRoles | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_ROLES_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionIncidentRoles, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_ROLES_VALUES!r}"
    )
