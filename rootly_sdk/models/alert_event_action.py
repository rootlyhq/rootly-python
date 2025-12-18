from typing import Literal, cast

AlertEventAction = Literal[
    "acknowledged",
    "added",
    "answered",
    "attached",
    "called",
    "created",
    "emailed",
    "escalated",
    "escalation_policy_paged",
    "ignored_alert_request",
    "marked",
    "muted",
    "not_marked",
    "notified",
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
    "called",
    "created",
    "emailed",
    "escalated",
    "escalation_policy_paged",
    "ignored_alert_request",
    "marked",
    "muted",
    "not_marked",
    "notified",
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


def check_alert_event_action(value: str) -> AlertEventAction:
    if value in ALERT_EVENT_ACTION_VALUES:
        return cast(AlertEventAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_EVENT_ACTION_VALUES!r}")
