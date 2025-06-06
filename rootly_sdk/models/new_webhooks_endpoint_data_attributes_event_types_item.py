from enum import Enum


class NewWebhooksEndpointDataAttributesEventTypesItem(str, Enum):
    ALERT_CREATED = "alert.created"
    GENIUS_WORKFLOW_RUN_CANCELED = "genius_workflow_run.canceled"
    GENIUS_WORKFLOW_RUN_COMPLETED = "genius_workflow_run.completed"
    GENIUS_WORKFLOW_RUN_FAILED = "genius_workflow_run.failed"
    GENIUS_WORKFLOW_RUN_QUEUED = "genius_workflow_run.queued"
    GENIUS_WORKFLOW_RUN_STARTED = "genius_workflow_run.started"
    INCIDENT_CANCELLED = "incident.cancelled"
    INCIDENT_CREATED = "incident.created"
    INCIDENT_DELETED = "incident.deleted"
    INCIDENT_IN_TRIAGE = "incident.in_triage"
    INCIDENT_MITIGATED = "incident.mitigated"
    INCIDENT_POST_MORTEM_CREATED = "incident_post_mortem.created"
    INCIDENT_POST_MORTEM_DELETED = "incident_post_mortem.deleted"
    INCIDENT_POST_MORTEM_PUBLISHED = "incident_post_mortem.published"
    INCIDENT_POST_MORTEM_UPDATED = "incident_post_mortem.updated"
    INCIDENT_RESOLVED = "incident.resolved"
    INCIDENT_SCHEDULED_COMPLETED = "incident.scheduled.completed"
    INCIDENT_SCHEDULED_CREATED = "incident.scheduled.created"
    INCIDENT_SCHEDULED_DELETED = "incident.scheduled.deleted"
    INCIDENT_SCHEDULED_IN_PROGRESS = "incident.scheduled.in_progress"
    INCIDENT_SCHEDULED_UPDATED = "incident.scheduled.updated"
    INCIDENT_UPDATED = "incident.updated"
    PULSE_CREATED = "pulse.created"

    def __str__(self) -> str:
        return str(self.value)
