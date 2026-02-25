from typing import Literal, cast

IncidentTriggerParamsIncidentConditionSummaryType1 = Literal["SET", "UNSET"]

INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES: set[
    IncidentTriggerParamsIncidentConditionSummaryType1
] = {
    "SET",
    "UNSET",
}


def check_incident_trigger_params_incident_condition_summary_type_1(
    value: str | None,
) -> IncidentTriggerParamsIncidentConditionSummaryType1 | None:
    if value is None:
        return None
    if value in INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES:
        return cast(IncidentTriggerParamsIncidentConditionSummaryType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_TRIGGER_PARAMS_INCIDENT_CONDITION_SUMMARY_TYPE_1_VALUES!r}"
    )
