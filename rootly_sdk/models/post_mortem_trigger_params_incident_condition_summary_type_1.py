from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionSummaryType1 = Literal["SET", "UNSET"]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES: set[
    PostMortemTriggerParamsIncidentConditionSummaryType1
] = {
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_summary_type_1(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionSummaryType1 | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionSummaryType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES!r}"
    )
