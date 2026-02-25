from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionResolvedAtType1 = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_TYPE_1_VALUES: set[
    PostMortemTriggerParamsIncidentConditionResolvedAtType1
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_resolved_at_type_1(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionResolvedAtType1 | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_TYPE_1_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionResolvedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_TYPE_1_VALUES!r}"
    )
