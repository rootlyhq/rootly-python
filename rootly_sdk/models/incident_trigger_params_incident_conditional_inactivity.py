from typing import Literal, cast

IncidentTriggerParamsIncidentConditionalInactivity = Literal["IS"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES: set[
    IncidentTriggerParamsIncidentConditionalInactivity
] = {
    "IS",
}


def check_incident_trigger_params_incident_conditional_inactivity(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionalInactivity | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionalInactivity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITIONAL_INACTIVITY_VALUES!r}"
    )
