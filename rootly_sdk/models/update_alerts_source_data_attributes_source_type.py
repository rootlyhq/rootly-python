from typing import Literal, cast

UpdateAlertsSourceDataAttributesSourceType = Literal[
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

UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES: set[UpdateAlertsSourceDataAttributesSourceType] = {
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


def check_update_alerts_source_data_attributes_source_type(
    value: str | None,
) -> UpdateAlertsSourceDataAttributesSourceType | None:
    if value is None:
        return None
    if value in UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES:
        return cast(UpdateAlertsSourceDataAttributesSourceType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ALERTS_SOURCE_DATA_ATTRIBUTES_SOURCE_TYPE_VALUES!r}"
    )
