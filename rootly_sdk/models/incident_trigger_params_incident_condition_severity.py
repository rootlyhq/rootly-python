from typing import Literal, cast

IncidentTriggerParamsIncidentConditionSeverity = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SEVERITY_VALUES: set[IncidentTriggerParamsIncidentConditionSeverity] = {
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


def check_incident_trigger_params_incident_condition_severity(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionSeverity | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SEVERITY_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionSeverity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SEVERITY_VALUES!r}"
    )
