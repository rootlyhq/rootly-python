from typing import Literal, cast

NewIncidentEventFunctionalityDataType = Literal["incident_event_functionalities"]

NEW_INCIDENT_EVENT_FUNCTIONALITY_DATA_TYPE_VALUES: set[NewIncidentEventFunctionalityDataType] = {
    "incident_event_functionalities",
}


def check_new_incident_event_functionality_data_type(value: str | None) -> NewIncidentEventFunctionalityDataType | None:
    if value is None:
        return None
    if value in NEW_INCIDENT_EVENT_FUNCTIONALITY_DATA_TYPE_VALUES:
        return cast(NewIncidentEventFunctionalityDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_INCIDENT_EVENT_FUNCTIONALITY_DATA_TYPE_VALUES!r}"
    )
