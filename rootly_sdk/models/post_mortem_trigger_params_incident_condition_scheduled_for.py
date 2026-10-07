from typing import Literal

PostMortemTriggerParamsIncidentConditionScheduledFor = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES: set[
    PostMortemTriggerParamsIncidentConditionScheduledFor
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_scheduled_for(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionScheduledFor | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES!r}"
    )
