from typing import Literal

UpdateIncidentPostMortemDataType = Literal["incident_post_mortems"]

UPDATE_INCIDENT_POST_MORTEM_DATA_TYPE_VALUES: set[UpdateIncidentPostMortemDataType] = {
    "incident_post_mortems",
}


def check_update_incident_post_mortem_data_type(value: str | None) -> UpdateIncidentPostMortemDataType | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_POST_MORTEM_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_POST_MORTEM_DATA_TYPE_VALUES!r}")
