from typing import Literal, cast

IncidentTriggerParamsIncidentConditionDetectedAtType1 = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES: set[
    IncidentTriggerParamsIncidentConditionDetectedAtType1
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_detected_at_type_1(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionDetectedAtType1 | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionDetectedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_DETECTED_AT_TYPE_1_VALUES!r}"
    )
