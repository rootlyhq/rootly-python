from typing import Literal, cast

PostMortemTriggerParamsIncidentCondition = Literal["ALL", "ANY", "NONE"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES: set[PostMortemTriggerParamsIncidentCondition] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_post_mortem_trigger_params_incident_condition(value: str | None) -> PostMortemTriggerParamsIncidentCondition | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES:
        return cast(PostMortemTriggerParamsIncidentCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES!r}"
    )
