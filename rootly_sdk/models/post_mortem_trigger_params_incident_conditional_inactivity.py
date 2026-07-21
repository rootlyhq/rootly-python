from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionalInactivity = Literal["IS"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES: set[
    PostMortemTriggerParamsIncidentConditionalInactivity
] = {
    "IS",
}


def check_post_mortem_trigger_params_incident_conditional_inactivity(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionalInactivity | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionalInactivity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES!r}"
    )
