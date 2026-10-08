from typing import Literal

PostMortemTriggerParamsIncidentConditionDetectedAt = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES: set[
    PostMortemTriggerParamsIncidentConditionDetectedAt
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_detected_at(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionDetectedAt | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES!r}"
    )
