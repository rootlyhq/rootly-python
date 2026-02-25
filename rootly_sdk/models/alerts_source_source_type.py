from typing import Literal, cast

AlertsSourceSourceType = Literal[
    "alertmanager",
    "app_dynamics",
    "app_optics",
    "azure",
    "bug_snag",
    "catchpoint",
    "checkly",
    "chronosphere",
    "cloud_watch",
    "datadog",
    "email",
    "generic_webhook",
    "google_cloud",
    "grafana",
    "honeycomb",
    "monte_carlo",
    "nagios",
    "new_relic",
    "prtg",
    "sentry",
    "splunk",
]

ALERTS_SOURCE_SOURCE_TYPE_VALUES: set[AlertsSourceSourceType] = {
    "alertmanager",
    "app_dynamics",
    "app_optics",
    "azure",
    "bug_snag",
    "catchpoint",
    "checkly",
    "chronosphere",
    "cloud_watch",
    "datadog",
    "email",
    "generic_webhook",
    "google_cloud",
    "grafana",
    "honeycomb",
    "monte_carlo",
    "nagios",
    "new_relic",
    "prtg",
    "sentry",
    "splunk",
}


def check_alerts_source_source_type(value: str | None) -> AlertsSourceSourceType | None:
    if value is None:
        return None
    if value in ALERTS_SOURCE_SOURCE_TYPE_VALUES:
        return cast(AlertsSourceSourceType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERTS_SOURCE_SOURCE_TYPE_VALUES!r}")
