from typing import Literal, cast

IncidentPostMortemStatus = Literal["draft", "published"]

INCIDENT_POST_MORTEM_STATUS_VALUES: set[IncidentPostMortemStatus] = {
    "draft",
    "published",
}


def check_incident_post_mortem_status(value: str | None) -> IncidentPostMortemStatus | None:
    if value is None:
        return None
    if value in INCIDENT_POST_MORTEM_STATUS_VALUES:
        return cast(IncidentPostMortemStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_POST_MORTEM_STATUS_VALUES!r}")
