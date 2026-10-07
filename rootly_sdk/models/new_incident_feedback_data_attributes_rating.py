from typing import Literal

NewIncidentFeedbackDataAttributesRating = Literal[0, 1, 2, 3, 4]

NEW_INCIDENT_FEEDBACK_DATA_ATTRIBUTES_RATING_VALUES: set[NewIncidentFeedbackDataAttributesRating] = {
    0,
    1,
    2,
    3,
    4,
}


def check_new_incident_feedback_data_attributes_rating(value: int) -> NewIncidentFeedbackDataAttributesRating:
    if value in NEW_INCIDENT_FEEDBACK_DATA_ATTRIBUTES_RATING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_FEEDBACK_DATA_ATTRIBUTES_RATING_VALUES!r}"
    )
