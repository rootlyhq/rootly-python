from typing import Literal

PostMortemTriggerParamsIncidentConditionScheduledUntil = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES: set[
    PostMortemTriggerParamsIncidentConditionScheduledUntil
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_scheduled_until(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionScheduledUntil | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES!r}"
    )
