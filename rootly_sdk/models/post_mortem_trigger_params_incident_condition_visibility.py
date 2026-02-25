from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionVisibility = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES: set[
    PostMortemTriggerParamsIncidentConditionVisibility
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


def check_post_mortem_trigger_params_incident_condition_visibility(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionVisibility | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionVisibility, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES!r}"
    )
