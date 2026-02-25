from typing import Literal, cast

IncidentFeedbackListDataItemType = Literal["incident_feedbacks"]

INCIDENT_FEEDBACK_LIST_DATA_ITEM_TYPE_VALUES: set[IncidentFeedbackListDataItemType] = {
    "incident_feedbacks",
}


def check_incident_feedback_list_data_item_type(value: str | None) -> IncidentFeedbackListDataItemType | None:
    if value is None:
        return None
    if value in INCIDENT_FEEDBACK_LIST_DATA_ITEM_TYPE_VALUES:
        return cast(IncidentFeedbackListDataItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_FEEDBACK_LIST_DATA_ITEM_TYPE_VALUES!r}")
