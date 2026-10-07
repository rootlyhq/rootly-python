from typing import Literal

IncidentTriggerParamsIncidentConditionStartedAt = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES: set[IncidentTriggerParamsIncidentConditionStartedAt] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_started_at(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionStartedAt | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_VALUES!r}"
    )
