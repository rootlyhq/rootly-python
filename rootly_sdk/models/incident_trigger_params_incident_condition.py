from typing import Literal, cast

IncidentTriggerParamsIncidentCondition = Literal["ALL", "ANY", "NONE"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES: set[IncidentTriggerParamsIncidentCondition] = {
    "ALL",
    "ANY",
    "NONE",
}


def check_incident_trigger_params_incident_condition(
    value: str | None,
) -> IncidentTriggerParamsIncidentCondition | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES:
        return cast(IncidentTriggerParamsIncidentCondition, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_VALUES!r}"
    )
