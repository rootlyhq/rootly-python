from typing import Literal

UpdateIncidentFeedbackDataType = Literal["incident_feedbacks"]

UPDATE_INCIDENT_FEEDBACK_DATA_TYPE_VALUES: set[UpdateIncidentFeedbackDataType] = {
    "incident_feedbacks",
}


def check_update_incident_feedback_data_type(value: str | None) -> UpdateIncidentFeedbackDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_FEEDBACK_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_FEEDBACK_DATA_TYPE_VALUES!r}")
