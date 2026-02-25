from typing import Literal, cast

IncidentTriggerParamsIncidentConditionStatus = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STATUS_VALUES: set[IncidentTriggerParamsIncidentConditionStatus] = {
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


def check_incident_trigger_params_incident_condition_status(value: str | None) -> IncidentTriggerParamsIncidentConditionStatus | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STATUS_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STATUS_VALUES!r}"
    )
