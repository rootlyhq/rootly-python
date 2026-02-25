from typing import Literal, cast

ListIncidentAlertsInclude = Literal[
    "alert_call_recording",
    "alert_field_values",
    "alert_group",
    "alert_urgency",
    "alerting_targets",
    "environments",
    "escalation_policies",
    "events",
    "group_leader_alert",
    "group_member_alerts",
    "groups",
    "heartbeat",
    "incidents",
    "live_call_router",
    "responders",
    "services",
]

LIST_INCIDENT_ALERTS_INCLUDE_VALUES: set[ListIncidentAlertsInclude] = {
    "alert_call_recording",
    "alert_field_values",
    "alert_group",
    "alert_urgency",
    "alerting_targets",
    "environments",
    "escalation_policies",
    "events",
    "group_leader_alert",
    "group_member_alerts",
    "groups",
    "heartbeat",
    "incidents",
    "live_call_router",
    "responders",
    "services",
}


def check_list_incident_alerts_include(value: str | None) -> ListIncidentAlertsInclude | None:
    if value is None:
        return None
    if value in LIST_INCIDENT_ALERTS_INCLUDE_VALUES:
        return cast(ListIncidentAlertsInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_ALERTS_INCLUDE_VALUES!r}")
