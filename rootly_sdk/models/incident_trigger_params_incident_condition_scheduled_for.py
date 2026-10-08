from typing import Literal

IncidentTriggerParamsIncidentConditionScheduledFor = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES: set[
    IncidentTriggerParamsIncidentConditionScheduledFor
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_scheduled_for(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionScheduledFor | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_FOR_VALUES!r}"
    )
