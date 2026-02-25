from typing import Literal, cast

IncidentTriggerParamsIncidentPostMortemConditionCause = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_CAUSE_VALUES: set[
    IncidentTriggerParamsIncidentPostMortemConditionCause
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


def check_incident_trigger_params_incident_post_mortem_condition_cause(
    value: str | None,
) -> IncidentTriggerParamsIncidentPostMortemConditionCause | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_CAUSE_VALUES:
        return cast(IncidentTriggerParamsIncidentPostMortemConditionCause, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_POST_MORTEM_CONDITION_CAUSE_VALUES!r}"
    )
