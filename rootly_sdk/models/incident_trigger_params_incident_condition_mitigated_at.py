from typing import Literal, cast

IncidentTriggerParamsIncidentConditionMitigatedAt = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES: set[
    IncidentTriggerParamsIncidentConditionMitigatedAt
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_mitigated_at(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionMitigatedAt | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionMitigatedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_MITIGATED_AT_VALUES!r}"
    )
