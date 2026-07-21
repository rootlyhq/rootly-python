from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionStartedAt = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES: set[
    PostMortemTriggerParamsIncidentConditionStartedAt
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_started_at(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionStartedAt | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionStartedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES!r}"
    )
