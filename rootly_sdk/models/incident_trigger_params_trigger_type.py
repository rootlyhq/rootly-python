from typing import Literal, cast

IncidentTriggerParamsTriggerType = Literal["incident"]

INCIDENT_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES: set[IncidentTriggerParamsTriggerType] = {
    "incident",
}


def check_incident_trigger_params_trigger_type(value: str | None) -> IncidentTriggerParamsTriggerType | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES:
        return cast(IncidentTriggerParamsTriggerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_TRIGGER_TYPE_VALUES!r}")
