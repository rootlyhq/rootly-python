from typing import Literal, cast

IncidentTriggerParamsIncidentConditionVisibility = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES: set[IncidentTriggerParamsIncidentConditionVisibility] = {
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


def check_incident_trigger_params_incident_condition_visibility(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionVisibility | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionVisibility, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_VISIBILITY_VALUES!r}"
    )
