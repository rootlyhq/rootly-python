from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionFunctionality = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_FUNCTIONALITY_VALUES: set[
    PostMortemTriggerParamsIncidentConditionFunctionality
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


def check_post_mortem_trigger_params_incident_condition_functionality(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionFunctionality | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_FUNCTIONALITY_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionFunctionality, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_FUNCTIONALITY_VALUES!r}"
    )
