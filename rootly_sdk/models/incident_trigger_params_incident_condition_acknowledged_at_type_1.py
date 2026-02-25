from typing import Literal, cast

IncidentTriggerParamsIncidentConditionAcknowledgedAtType1 = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES: set[
    IncidentTriggerParamsIncidentConditionAcknowledgedAtType1
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_acknowledged_at_type_1(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionAcknowledgedAtType1 | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionAcknowledgedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_ACKNOWLEDGED_AT_TYPE_1_VALUES!r}"
    )
