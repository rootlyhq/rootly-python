from typing import Literal, cast

UpdateIncidentPostMortemDataAttributesStatus = Literal["draft", "published"]

UPDATE_INCIDENT_POST_MORTEM_DATA_ATTRIBUTES_STATUS_VALUES: set[UpdateIncidentPostMortemDataAttributesStatus] = {
    "draft",
    "published",
}


def check_update_incident_post_mortem_data_attributes_status(
    value: str | None,
) -> UpdateIncidentPostMortemDataAttributesStatus | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_POST_MORTEM_DATA_ATTRIBUTES_STATUS_VALUES:
        return cast(UpdateIncidentPostMortemDataAttributesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_POST_MORTEM_DATA_ATTRIBUTES_STATUS_VALUES!r}"
    )
