from typing import Literal

PublishIncidentTaskParamsSelectedComponentStatusesAdditionalProperty = Literal[
    "degraded_performance", "major_outage", "operational", "partial_outage"
]

PUBLISH_INCIDENT_TASK_PARAMS_SELECTED_COMPONENT_STATUSES_ADDITIONAL_PROPERTY_VALUES: set[
    PublishIncidentTaskParamsSelectedComponentStatusesAdditionalProperty
] = {
    "degraded_performance",
    "major_outage",
    "operational",
    "partial_outage",
}


def check_publish_incident_task_params_selected_component_statuses_additional_property(
    value: str | None,
) -> PublishIncidentTaskParamsSelectedComponentStatusesAdditionalProperty | None:
    if value is None:
        return None
    if value in PUBLISH_INCIDENT_TASK_PARAMS_SELECTED_COMPONENT_STATUSES_ADDITIONAL_PROPERTY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUBLISH_INCIDENT_TASK_PARAMS_SELECTED_COMPONENT_STATUSES_ADDITIONAL_PROPERTY_VALUES!r}"
    )
