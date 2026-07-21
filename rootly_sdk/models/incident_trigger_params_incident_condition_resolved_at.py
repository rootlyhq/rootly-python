from typing import Literal, cast

IncidentTriggerParamsIncidentConditionResolvedAt = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES: set[IncidentTriggerParamsIncidentConditionResolvedAt] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_resolved_at(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionResolvedAt | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionResolvedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_RESOLVED_AT_VALUES!r}"
    )
