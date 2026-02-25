from typing import Literal, cast

IncidentPostMortemResponseDataType = Literal["incident_post_mortems"]

INCIDENT_POST_MORTEM_RESPONSE_DATA_TYPE_VALUES: set[IncidentPostMortemResponseDataType] = {
    "incident_post_mortems",
}


def check_incident_post_mortem_response_data_type(value: str | None) -> IncidentPostMortemResponseDataType | None:
    if value is None:
        return None
    if value in INCIDENT_POST_MORTEM_RESPONSE_DATA_TYPE_VALUES:
        return cast(IncidentPostMortemResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_POST_MORTEM_RESPONSE_DATA_TYPE_VALUES!r}")
