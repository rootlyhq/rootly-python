from typing import Literal, cast

IncidentTriggerParamsIncidentConditionIncidentType = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES: set[
    IncidentTriggerParamsIncidentConditionIncidentType
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


def check_incident_trigger_params_incident_condition_incident_type(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionIncidentType | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionIncidentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_INCIDENT_TYPE_VALUES!r}"
    )
