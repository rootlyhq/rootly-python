from typing import Literal, cast

UpdateIncidentRetrospectiveStepDataType = Literal["incident_retrospective_steps"]

UPDATE_INCIDENT_RETROSPECTIVE_STEP_DATA_TYPE_VALUES: set[UpdateIncidentRetrospectiveStepDataType] = {
    "incident_retrospective_steps",
}


def check_update_incident_retrospective_step_data_type(value: str | None) -> UpdateIncidentRetrospectiveStepDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_RETROSPECTIVE_STEP_DATA_TYPE_VALUES:
        return cast(UpdateIncidentRetrospectiveStepDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_RETROSPECTIVE_STEP_DATA_TYPE_VALUES!r}"
    )
