from typing import Literal, cast

AlertEventAction = Literal[
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

ALERT_EVENT_ACTION_VALUES: set[AlertEventAction] = {
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


def check_alert_event_action(value: str | None) -> AlertEventAction | None:
    if value is None:
        return None
    if value in ALERT_EVENT_ACTION_VALUES:
        return cast(AlertEventAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_EVENT_ACTION_VALUES!r}")
