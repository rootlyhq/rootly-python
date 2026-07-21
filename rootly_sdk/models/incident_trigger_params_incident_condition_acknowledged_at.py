from typing import Literal, cast

IncidentTriggerParamsIncidentConditionAcknowledgedAt = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_VALUES: set[
    IncidentTriggerParamsIncidentConditionAcknowledgedAt
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_acknowledged_at(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionAcknowledgedAt | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionAcknowledgedAt, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_VALUES!r}"
    )
