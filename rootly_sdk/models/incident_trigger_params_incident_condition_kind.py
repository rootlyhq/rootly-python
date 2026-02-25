from typing import Literal, cast

IncidentTriggerParamsIncidentConditionKind = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_KIND_VALUES: set[IncidentTriggerParamsIncidentConditionKind] = {
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


def check_incident_trigger_params_incident_condition_kind(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionKind | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_KIND_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_KIND_VALUES!r}"
    )
