from typing import Literal, cast

IncidentTriggerParamsIncidentConditionLabel = Literal[
    "ANY", "CONTAINS", "CONTAINS_ALL", "CONTAINS_NONE", "IS", "IS NOT", "NONE", "SET", "UNSET"
]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES: set[IncidentTriggerParamsIncidentConditionLabel] = {
    "ANY",
    "CONTAINS",
    "CONTAINS_ALL",
    "CONTAINS_NONE",
    "IS",
    "IS NOT",
    "NONE",
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_label(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionLabel | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionLabel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_LABEL_VALUES!r}"
    )
