from typing import Literal, cast

NewIncidentFeedbackDataType = Literal["incident_feedbacks"]

NEW_INCIDENT_FEEDBACK_DATA_TYPE_VALUES: set[NewIncidentFeedbackDataType] = {
    "incident_feedbacks",
}


def check_new_incident_feedback_data_type(value: str | None) -> NewIncidentFeedbackDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_FEEDBACK_DATA_TYPE_VALUES:
        return cast(NewIncidentFeedbackDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_FEEDBACK_DATA_TYPE_VALUES!r}")
