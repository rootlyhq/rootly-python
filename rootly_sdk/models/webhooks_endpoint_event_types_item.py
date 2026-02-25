from typing import Literal, cast

WebhooksEndpointEventTypesItem = Literal[
    "alert.created",
    "genius_workflow_run.canceled",
    "genius_workflow_run.completed",
    "genius_workflow_run.failed",
    "genius_workflow_run.queued",
    "genius_workflow_run.started",
    "incident.cancelled",
    "incident.created",
    "incident.deleted",
    "incident.in_triage",
    "incident.mitigated",
    "incident.resolved",
    "incident.scheduled.completed",
    "incident.scheduled.created",
    "incident.scheduled.deleted",
    "incident.scheduled.in_progress",
    "incident.scheduled.updated",
    "incident.updated",
    "incident_event.created",
    "incident_event.deleted",
    "incident_event.updated",
    "incident_post_mortem.created",
    "incident_post_mortem.deleted",
    "incident_post_mortem.published",
    "incident_post_mortem.updated",
    "incident_status_page_event.created",
    "incident_status_page_event.deleted",
    "incident_status_page_event.updated",
    "pulse.created",
]

WEBHOOKS_ENDPOINT_EVENT_TYPES_ITEM_VALUES: set[WebhooksEndpointEventTypesItem] = {
    "alert.created",
    "genius_workflow_run.canceled",
    "genius_workflow_run.completed",
    "genius_workflow_run.failed",
    "genius_workflow_run.queued",
    "genius_workflow_run.started",
    "incident.cancelled",
    "incident.created",
    "incident.deleted",
    "incident.in_triage",
    "incident.mitigated",
    "incident.resolved",
    "incident.scheduled.completed",
    "incident.scheduled.created",
    "incident.scheduled.deleted",
    "incident.scheduled.in_progress",
    "incident.scheduled.updated",
    "incident.updated",
    "incident_event.created",
    "incident_event.deleted",
    "incident_event.updated",
    "incident_post_mortem.created",
    "incident_post_mortem.deleted",
    "incident_post_mortem.published",
    "incident_post_mortem.updated",
    "incident_status_page_event.created",
    "incident_status_page_event.deleted",
    "incident_status_page_event.updated",
    "pulse.created",
}


def check_webhooks_endpoint_event_types_item(value: str | None) -> WebhooksEndpointEventTypesItem | None:
    if value is None:
        return None
    if value in WEBHOOKS_ENDPOINT_EVENT_TYPES_ITEM_VALUES:
        return cast(WebhooksEndpointEventTypesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOKS_ENDPOINT_EVENT_TYPES_ITEM_VALUES!r}")
