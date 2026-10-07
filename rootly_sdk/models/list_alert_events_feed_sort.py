from typing import Literal

ListAlertEventsFeedSort = Literal["-created_at", "created_at"]

LIST_ALERT_EVENTS_FEED_SORT_VALUES: set[ListAlertEventsFeedSort] = {
    "-created_at",
    "created_at",
}


def check_list_alert_events_feed_sort(value: str | None) -> ListAlertEventsFeedSort | None:
    if value is None:
        return None
    if value in LIST_ALERT_EVENTS_FEED_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_EVENTS_FEED_SORT_VALUES!r}")
