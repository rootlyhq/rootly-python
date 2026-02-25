from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionDetectedAtType1 = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES: set[
    PostMortemTriggerParamsIncidentConditionDetectedAtType1
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_detected_at_type_1(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionDetectedAtType1 | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionDetectedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES!r}"
    )
