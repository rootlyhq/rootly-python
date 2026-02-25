from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionEnvironment = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ENVIRONMENT_VALUES: set[
    PostMortemTriggerParamsIncidentConditionEnvironment
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


def check_post_mortem_trigger_params_incident_condition_environment(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionEnvironment | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ENVIRONMENT_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionEnvironment, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_ENVIRONMENT_VALUES!r}"
    )
