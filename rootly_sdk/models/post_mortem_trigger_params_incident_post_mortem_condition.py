from typing import Literal, cast

PostMortemTriggerParamsIncidentPostMortemCondition = Literal["ALL", "ANY", "NONE"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_VALUES: set[
    PostMortemTriggerParamsIncidentPostMortemCondition
] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_post_mortem_trigger_params_incident_post_mortem_condition(
    value: str | None,
) -> PostMortemTriggerParamsIncidentPostMortemCondition | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_VALUES:
        return cast(PostMortemTriggerParamsIncidentPostMortemCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_VALUES!r}"
    )
