from typing import Literal, cast

IncidentTriggerParamsIncidentConditionGroup = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_GROUP_VALUES: set[IncidentTriggerParamsIncidentConditionGroup] = {
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


def check_incident_trigger_params_incident_condition_group(value: str | None) -> IncidentTriggerParamsIncidentConditionGroup | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_GROUP_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionGroup, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_GROUP_VALUES!r}"
    )
