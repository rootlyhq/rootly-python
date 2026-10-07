from typing import Literal

IncidentTriggerParamsIncidentConditionDetectedAt = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES: set[IncidentTriggerParamsIncidentConditionDetectedAt] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_detected_at(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionDetectedAt | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_VALUES!r}"
    )
