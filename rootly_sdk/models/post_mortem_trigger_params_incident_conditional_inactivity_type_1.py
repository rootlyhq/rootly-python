from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionalInactivityType1 = Literal["IS"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_TYPE_1_VALUES: set[
    PostMortemTriggerParamsIncidentConditionalInactivityType1
] = {
    "IS",
}


def check_post_mortem_trigger_params_incident_conditional_inactivity_type_1(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionalInactivityType1 | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_TYPE_1_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionalInactivityType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_TYPE_1_VALUES!r}"
    )
