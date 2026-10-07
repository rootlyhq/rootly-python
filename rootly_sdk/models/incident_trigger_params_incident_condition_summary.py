from typing import Literal

IncidentTriggerParamsIncidentConditionSummary = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES: set[IncidentTriggerParamsIncidentConditionSummary] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_summary(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionSummary | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_VALUES!r}"
    )
