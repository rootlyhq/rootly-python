from typing import Literal, cast

GetAlertInclude = Literal[
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

GET_ALERT_INCLUDE_VALUES: set[GetAlertInclude] = {
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


def check_get_alert_include(value: str | None) -> GetAlertInclude | None:
    if value is None:
        return None
    if value in GET_ALERT_INCLUDE_VALUES:
        return cast(GetAlertInclude, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_ALERT_INCLUDE_VALUES!r}")
