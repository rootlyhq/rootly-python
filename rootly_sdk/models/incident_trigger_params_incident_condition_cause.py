from typing import Literal, cast

IncidentTriggerParamsIncidentConditionCause = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_CAUSE_VALUES: set[IncidentTriggerParamsIncidentConditionCause] = {
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


def check_incident_trigger_params_incident_condition_cause(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionCause | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_CAUSE_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionCause, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_CAUSE_VALUES!r}"
    )
