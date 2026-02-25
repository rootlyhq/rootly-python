from typing import Literal, cast

PostMortemTriggerParamsIncidentPostMortemConditionCause = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_CAUSE_VALUES: set[
    PostMortemTriggerParamsIncidentPostMortemConditionCause
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


def check_post_mortem_trigger_params_incident_post_mortem_condition_cause(
    value: str | None,
) -> PostMortemTriggerParamsIncidentPostMortemConditionCause | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_CAUSE_VALUES:
        return cast(PostMortemTriggerParamsIncidentPostMortemConditionCause, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_CAUSE_VALUES!r}"
    )
