from typing import Literal

IncidentPostMortemShowTimelineOrder = Literal["asc", "desc"]

INCIDENT_POST_MORTEM_SHOW_TIMELINE_ORDER_VALUES: set[IncidentPostMortemShowTimelineOrder] = {
    "asc",
    "desc",
}


def check_incident_post_mortem_show_timeline_order(value: str | None) -> IncidentPostMortemShowTimelineOrder | None:
    if value is None:
        return None
    if value in INCIDENT_POST_MORTEM_SHOW_TIMELINE_ORDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_POST_MORTEM_SHOW_TIMELINE_ORDER_VALUES!r}")
