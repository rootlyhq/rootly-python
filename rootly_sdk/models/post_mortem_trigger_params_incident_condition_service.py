from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionService = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SERVICE_VALUES: set[PostMortemTriggerParamsIncidentConditionService] = {
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


def check_post_mortem_trigger_params_incident_condition_service(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionService | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SERVICE_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionService, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SERVICE_VALUES!r}"
    )
