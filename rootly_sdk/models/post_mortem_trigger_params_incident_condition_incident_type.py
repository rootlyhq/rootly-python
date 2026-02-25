from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionIncidentType = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES: set[
    PostMortemTriggerParamsIncidentConditionIncidentType
] = {
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


def check_post_mortem_trigger_params_incident_condition_incident_type(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionIncidentType | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionIncidentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES!r}"
    )
