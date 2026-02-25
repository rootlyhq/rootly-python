from typing import Literal, cast

PostMortemTriggerParamsIncidentConditionSubStatus = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUB_STATUS_VALUES: set[
    PostMortemTriggerParamsIncidentConditionSubStatus
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


def check_post_mortem_trigger_params_incident_condition_sub_status(
    value: str | None,
) -> PostMortemTriggerParamsIncidentConditionSubStatus | None:
    if value is None:
        return None
    if value in POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUB_STATUS_VALUES:
        return cast(PostMortemTriggerParamsIncidentConditionSubStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MORTEM_TRIGGER_PARAMS_INCIDENT_CONDITION_SUB_STATUS_VALUES!r}"
    )
