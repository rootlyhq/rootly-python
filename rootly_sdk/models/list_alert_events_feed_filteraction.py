from typing import Literal, cast

ListAlertEventsFeedFilteraction = Literal[
    "acknowledged",
    "added",
    "answered",
    "attached",
    "call_lifecycle",
    "called",
    "created",
    "deferred",
    "emailed",
    "escalated",
    "escalation_policy_paged",
    "google_chat_messaged",
    "ignored_alert_request",
    "level_skipped",
    "marked",
    "ms_teams_messaged",
    "muted",
    "not_marked",
    "notified",
    "open",
    "opened",
    "paged",
    "removed",
    "resolved",
    "retriggered",
    "skipped",
    "slacked",
    "snoozed",
    "texted",
    "triggered",
    "updated",
]

LIST_ALERT_EVENTS_FEED_FILTERACTION_VALUES: set[ListAlertEventsFeedFilteraction] = {
    "acknowledged",
    "added",
    "answered",
    "attached",
    "call_lifecycle",
    "called",
    "created",
    "deferred",
    "emailed",
    "escalated",
    "escalation_policy_paged",
    "google_chat_messaged",
    "ignored_alert_request",
    "level_skipped",
    "marked",
    "ms_teams_messaged",
    "muted",
    "not_marked",
    "notified",
    "open",
    "opened",
    "paged",
    "removed",
    "resolved",
    "retriggered",
    "skipped",
    "slacked",
    "snoozed",
    "texted",
    "triggered",
    "updated",
}


def check_list_alert_events_feed_filteraction(value: str | None) -> ListAlertEventsFeedFilteraction | None:
    if value is None:
        return None
    if value in LIST_ALERT_EVENTS_FEED_FILTERACTION_VALUES:
        return cast(ListAlertEventsFeedFilteraction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_EVENTS_FEED_FILTERACTION_VALUES!r}")
