from typing import Literal, cast

IncidentEventFunctionalityResponseDataType = Literal["incident_event_functionalities"]

INCIDENT_EVENT_FUNCTIONALITY_RESPONSE_DATA_TYPE_VALUES: set[IncidentEventFunctionalityResponseDataType] = {
    "incident_event_functionalities",
}


def check_incident_event_functionality_response_data_type(value: str | None) -> IncidentEventFunctionalityResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_EVENT_FUNCTIONALITY_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentEventFunctionalityResponseDataType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INCIDENT_EVENT_FUNCTIONALITY_RESPONSE_DATA_TYPE_VALUES!r}"
    )
