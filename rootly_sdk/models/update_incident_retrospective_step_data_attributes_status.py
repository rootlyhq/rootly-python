from typing import Literal, cast

UpdateIncidentRetrospectiveStepDataAttributesStatus = Literal["completed", "in_progress", "skipped", "todo"]

UPDATE_INCIDENT_RETROSPECTIVE_STEP_DATA_ATTRIBUTES_STATUS_VALUES: set[
    UpdateIncidentRetrospectiveStepDataAttributesStatus
] = {
    "completed",
    "in_progress",
    "skipped",
    "todo",
}


def check_update_incident_retrospective_step_data_attributes_status(
    value: str | None,
) -> UpdateIncidentRetrospectiveStepDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_RETROSPECTIVE_STEP_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(UpdateIncidentRetrospectiveStepDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_RETROSPECTIVE_STEP_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
