from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionMitigatedAt = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES: set[
    PostMortemTriggerParamsIncidentConditionMitigatedAt
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_mitigated_at(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionMitigatedAt | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionMitigatedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES!r}"
    )
