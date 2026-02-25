from typing import Literal, cast

IncidentRetrospectiveStepResponseDataType = Literal["incident_retrospective_steps"]

INCIDENT_RETROSPECTIVE_STEP_RESPONSE_DATA_TYPE_VALUES: set[IncidentRetrospectiveStepResponseDataType] = {
    "incident_retrospective_steps",
}


def check_incident_retrospective_step_response_data_type(value: str | None) -> IncidentRetrospectiveStepResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_RETROSPECTIVE_STEP_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentRetrospectiveStepResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_RETROSPECTIVE_STEP_RESPONSE_DATA_TYPE_VALUES!r}"
    )
