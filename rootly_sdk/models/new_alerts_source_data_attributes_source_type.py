from typing import Literal

NewAlertsSourceDataAttributesSourceType = Literal[
    "alertmanager",
    "app_dynamics",
    "app_optics",
    "aws_sns",
    "azure",
    "bug_snag",
    "catchpoint",
    "checkly",
    "chronosphere",
    "cloud_watch",
    "cloudflare",
    "datadog",
    "dynatrace",
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

NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES: set[NewAlertsSourceDataAttributesSourceType] = {
    "alertmanager",
    "app_dynamics",
    "app_optics",
    "aws_sns",
    "azure",
    "bug_snag",
    "catchpoint",
    "checkly",
    "chronosphere",
    "cloud_watch",
    "cloudflare",
    "datadog",
    "dynatrace",
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


def check_new_alerts_source_data_attributes_source_type(
    value: str | None,
) -> NewAlertsSourceDataAttributesSourceType | None:
    if value is None:
        return None
    if value in NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NEW_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES!r}"
    )
