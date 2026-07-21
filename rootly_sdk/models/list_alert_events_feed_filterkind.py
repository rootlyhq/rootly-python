from typing import Literal, cast

ListAlertEventsFeedFilterkind = Literal[
    "action",
    "alert_grouping",
    "alert_routing",
    "alert_urgency",
    "deferral",
    "informational",
    "maintenance",
    "noise",
    "note",
    "notification",
    "recording",
    "status_update",
]

LIST_ALERT_EVENTS_FEED_FILTERKIND_VALUES: set[ListAlertEventsFeedFilterkind] = {
    "action",
    "alert_grouping",
    "alert_routing",
    "alert_urgency",
    "deferral",
    "informational",
    "maintenance",
    "noise",
    "note",
    "notification",
    "recording",
    "status_update",
}


def check_list_alert_events_feed_filterkind(value: str | None) -> ListAlertEventsFeedFilterkind | None:
    if value is None:
        return None
    if value in LIST_ALERT_EVENTS_FEED_FILTERKIND_VALUES:
        return cast(ListAlertEventsFeedFilterkind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_EVENTS_FEED_FILTERKIND_VALUES!r}")
