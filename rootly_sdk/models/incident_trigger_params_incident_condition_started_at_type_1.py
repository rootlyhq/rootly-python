from typing import Literal, cast

IncidentTriggerParamsIncidentConditionStartedAtType1 = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_TYPE_1_VALUES: set[
    IncidentTriggerParamsIncidentConditionStartedAtType1
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_started_at_type_1(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionStartedAtType1 | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_TYPE_1_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionStartedAtType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_STARTED_AT_TYPE_1_VALUES!r}"
    )
