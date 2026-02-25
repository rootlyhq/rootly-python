from typing import Literal, cast

UpdateIncidentEventFunctionalityDataType = Literal["incident_event_functionalities"]

UPDATE_INCIDENT_EVENT_FUNCTIONALITY_DATA_TYPE_VALUES: set[UpdateIncidentEventFunctionalityDataType] = {
    "incident_event_functionalities",
}


def check_update_incident_event_functionality_data_type(
    value: str | None,
) -> UpdateIncidentEventFunctionalityDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_EVENT_FUNCTIONALITY_DATA_TYPE_VALUES:
        return cast(UpdateIncidentEventFunctionalityDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_EVENT_FUNCTIONALITY_DATA_TYPE_VALUES!r}"
    )
