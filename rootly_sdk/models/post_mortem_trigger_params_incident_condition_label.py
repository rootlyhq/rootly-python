from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionLabel = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES: set[PostMortemTriggerParamsIncidentConditionLabel] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_post_mortem_trigger_params_incident_condition_label(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionLabel | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionLabel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES!r}"
    )
