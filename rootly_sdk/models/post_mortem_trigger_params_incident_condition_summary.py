from typing import Literal

PostMortemTriggerParamsIncidentConditionSummary = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES: set[PostMortemTriggerParamsIncidentConditionSummary] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_summary(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionSummary | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES!r}"
    )
