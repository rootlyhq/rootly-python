from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionKind = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_KIND_VALUES: set[PostMortemTriggerParamsIncidentConditionKind] = {
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


def check_post_mortem_trigger_params_incident_condition_kind(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionKind | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_KIND_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_KIND_VALUES!r}"
    )
