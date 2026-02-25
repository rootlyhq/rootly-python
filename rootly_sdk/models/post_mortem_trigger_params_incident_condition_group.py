from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionGroup = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_GROUP_VALUES: set[PostMortemTriggerParamsIncidentConditionGroup] = {
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


def check_post_mortem_trigger_params_incident_condition_group(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionGroup | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_GROUP_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionGroup, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_GROUP_VALUES!r}"
    )
