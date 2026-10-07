from typing import Literal

IncidentTriggerParamsIncidentConditionScheduledUntil = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES: set[
    IncidentTriggerParamsIncidentConditionScheduledUntil
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_scheduled_until(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionScheduledUntil | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SCHEDULED_UNTIL_VALUES!r}"
    )
