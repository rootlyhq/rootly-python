from typing import Literal

PostMortemTriggerParamsIncidentConditionResolvedAt = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES: set[
    PostMortemTriggerParamsIncidentConditionResolvedAt
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_resolved_at(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionResolvedAt | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES!r}"
    )
