from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_retrospective_progress_status import (
    IncidentRetrospectiveProgressStatus,
    check_incident_retrospective_progress_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_response import EnvironmentResponse
    from ..models.functionality_response import FunctionalityResponse
    from ..models.incident_cancelled_by_type_0 import IncidentCancelledByType0
    from ..models.incident_closed_by_type_0 import IncidentClosedByType0
    from ..models.incident_in_triage_by_type_0 import IncidentInTriageByType0
    from ..models.incident_labels_type_0 import IncidentLabelsType0
    from ..models.incident_mitigated_by_type_0 import IncidentMitigatedByType0
    from ..models.incident_resolved_by_type_0 import IncidentResolvedByType0
    from ..models.incident_started_by_type_0 import IncidentStartedByType0
    from ..models.incident_type_response import IncidentTypeResponse
    from ..models.incident_user_type_0 import IncidentUserType0
    from ..models.service_response import ServiceResponse
    from ..models.severity_response import SeverityResponse
    from ..models.team_response import TeamResponse


T = TypeVar("T", bound="Incident")


@_attrs_define
class Incident:
    """
    Attributes:
        title (str): The title of the incident
        created_at (str): Date of creation
        updated_at (str): Date of last update
        id (Union[Unset, str]): Unique ID of the incident
        sequential_id (Union[Unset, int]): Sequential ID of the incident
        kind (Union[Unset, str]): The kind of the incident
        slug (Union[Unset, str]): The slug of the incident
        parent_incident_id (Union[None, Unset, str]): ID of parent incident
        duplicate_incident_id (Union[None, Unset, str]): ID of duplicated incident
        summary (Union[None, Unset, str]): The summary of the incident
        private (Union[Unset, bool]): The visibility of the incident Default: False.
        source (Union[None, Unset, str]): The source of the incident
        status (Union[None, Unset, str]): The status of the incident
        url (Union[None, Unset, str]): The url to the incident
        short_url (Union[None, Unset, str]): The short url to the incident
        public_title (Union[None, Unset, str]): The public title of the incident
        user (Union['IncidentUserType0', None, Unset]): The user who created the incident
        severity (Union[Unset, SeverityResponse]):
        environments (Union[None, Unset, list['EnvironmentResponse']]): The Environments of the incident
        incident_types (Union[None, Unset, list['IncidentTypeResponse']]): The Incident Types of the incident
        services (Union[None, Unset, list['ServiceResponse']]): The Services of the incident
        functionalities (Union[None, Unset, list['FunctionalityResponse']]): The Functionalities of the incident
        groups (Union[None, Unset, list['TeamResponse']]): The Teams of to the incident
        labels (Union['IncidentLabelsType0', None, Unset]): Labels to attach to the incidents. eg: {"platform":"osx",
            "version": "1.29"}
        slack_channel_id (Union[None, Unset, str]): Slack channel id
        slack_channel_name (Union[None, Unset, str]): Slack channel name
        slack_channel_url (Union[None, Unset, str]): Slack channel url
        slack_channel_short_url (Union[None, Unset, str]): Slack channel short url
        slack_channel_deep_link (Union[None, Unset, str]): Slack channel deep link
        slack_channel_archived (Union[None, Unset, bool]): Whether the Slack channel is archived
        slack_last_message_ts (Union[None, Unset, str]): Timestamp of last Slack message
        zoom_meeting_id (Union[None, Unset, str]): Zoom meeting ID
        zoom_meeting_start_url (Union[None, Unset, str]): Zoom meeting start URL
        zoom_meeting_join_url (Union[None, Unset, str]): Zoom meeting join URL
        zoom_meeting_password (Union[None, Unset, str]): Zoom meeting password
        zoom_meeting_pstn_password (Union[None, Unset, str]): Zoom meeting PSTN password
        zoom_meeting_h323_password (Union[None, Unset, str]): Zoom meeting H323 password
        zoom_meeting_global_dial_in_numbers (Union[None, Unset, list[str]]): Zoom meeting global dial-in numbers
        google_drive_id (Union[None, Unset, str]): Google Drive document ID
        google_drive_parent_id (Union[None, Unset, str]): Google Drive parent folder ID
        google_drive_url (Union[None, Unset, str]): Google Drive URL
        google_meeting_id (Union[None, Unset, str]): Google meeting ID
        google_meeting_url (Union[None, Unset, str]): Google meeting URL
        jira_issue_key (Union[None, Unset, str]): Jira issue key
        jira_issue_id (Union[None, Unset, str]): Jira issue ID
        jira_issue_url (Union[None, Unset, str]): Jira issue URL
        github_issue_id (Union[None, Unset, str]): GitHub issue ID
        github_issue_url (Union[None, Unset, str]): GitHub issue URL
        gitlab_issue_id (Union[None, Unset, str]): GitLab issue ID
        gitlab_issue_url (Union[None, Unset, str]): GitLab issue URL
        asana_task_id (Union[None, Unset, str]): Asana task ID
        asana_task_url (Union[None, Unset, str]): Asana task URL
        linear_issue_id (Union[None, Unset, str]): Linear issue ID
        linear_issue_url (Union[None, Unset, str]): Linear issue URL
        trello_card_id (Union[None, Unset, str]): Trello card ID
        trello_card_url (Union[None, Unset, str]): Trello card URL
        zendesk_ticket_id (Union[None, Unset, str]): Zendesk ticket ID
        zendesk_ticket_url (Union[None, Unset, str]): Zendesk ticket URL
        pagerduty_incident_id (Union[None, Unset, str]): PagerDuty incident ID
        pagerduty_incident_number (Union[None, Unset, str]): PagerDuty incident number
        pagerduty_incident_url (Union[None, Unset, str]): PagerDuty incident URL
        opsgenie_incident_id (Union[None, Unset, str]): Opsgenie incident ID
        opsgenie_incident_url (Union[None, Unset, str]): Opsgenie incident URL
        opsgenie_alert_id (Union[None, Unset, str]): Opsgenie alert ID
        opsgenie_alert_url (Union[None, Unset, str]): Opsgenie alert URL
        service_now_incident_id (Union[None, Unset, str]): ServiceNow incident ID
        service_now_incident_key (Union[None, Unset, str]): ServiceNow incident key
        service_now_incident_url (Union[None, Unset, str]): ServiceNow incident URL
        mattermost_channel_id (Union[None, Unset, str]): Mattermost channel ID
        mattermost_channel_name (Union[None, Unset, str]): Mattermost channel name
        mattermost_channel_url (Union[None, Unset, str]): Mattermost channel URL
        confluence_page_id (Union[None, Unset, str]): Confluence page ID
        confluence_page_url (Union[None, Unset, str]): Confluence page URL
        datadog_notebook_id (Union[None, Unset, str]): Datadog notebook ID
        datadog_notebook_url (Union[None, Unset, str]): Datadog notebook URL
        shortcut_story_id (Union[None, Unset, str]): Shortcut story ID
        shortcut_story_url (Union[None, Unset, str]): Shortcut story URL
        shortcut_task_id (Union[None, Unset, str]): Shortcut task ID
        shortcut_task_url (Union[None, Unset, str]): Shortcut task URL
        motion_task_id (Union[None, Unset, str]): Motion task ID
        motion_task_url (Union[None, Unset, str]): Motion task URL
        clickup_task_id (Union[None, Unset, str]): ClickUp task ID
        clickup_task_url (Union[None, Unset, str]): ClickUp task URL
        victor_ops_incident_id (Union[None, Unset, str]): VictorOps incident ID
        victor_ops_incident_url (Union[None, Unset, str]): VictorOps incident URL
        quip_page_id (Union[None, Unset, str]): Quip page ID
        quip_page_url (Union[None, Unset, str]): Quip page URL
        sharepoint_page_id (Union[None, Unset, str]): SharePoint page ID
        sharepoint_page_url (Union[None, Unset, str]): SharePoint page URL
        airtable_base_key (Union[None, Unset, str]): Airtable base key
        airtable_table_name (Union[None, Unset, str]): Airtable table name
        airtable_record_id (Union[None, Unset, str]): Airtable record ID
        airtable_record_url (Union[None, Unset, str]): Airtable record URL
        freshservice_ticket_id (Union[None, Unset, str]): Freshservice ticket ID
        freshservice_ticket_url (Union[None, Unset, str]): Freshservice ticket URL
        freshservice_task_id (Union[None, Unset, str]): Freshservice task ID
        freshservice_task_url (Union[None, Unset, str]): Freshservice task URL
        mitigation_message (Union[None, Unset, str]): How was the incident mitigated?
        resolution_message (Union[None, Unset, str]): How was the incident resolved?
        cancellation_message (Union[None, Unset, str]): Why was the incident cancelled?
        scheduled_for (Union[None, Unset, str]): Date of when the maintenance begins
        scheduled_until (Union[None, Unset, str]): Date of when the maintenance ends
        muted_service_ids (Union[None, Unset, list[str]]): The Service IDs to mute alerts for during maintenance. Alerts
            for these services will still be triggered and attached to the incident, but won't page responders.
        retrospective_progress_status (Union[Unset, IncidentRetrospectiveProgressStatus]): The status of the
            retrospective progress
        in_triage_by (Union['IncidentInTriageByType0', None, Unset]): The user who triaged the incident
        started_by (Union['IncidentStartedByType0', None, Unset]): The user who started the incident
        mitigated_by (Union['IncidentMitigatedByType0', None, Unset]): The user who mitigated the incident
        resolved_by (Union['IncidentResolvedByType0', None, Unset]): The user who resolved the incident
        closed_by (Union['IncidentClosedByType0', None, Unset]): The user who closed the incident
        cancelled_by (Union['IncidentCancelledByType0', None, Unset]): The user who cancelled the incident
        in_triage_at (Union[None, Unset, str]): Date of triage
        started_at (Union[None, Unset, str]): Date of start
        detected_at (Union[None, Unset, str]): Date of detection
        acknowledged_at (Union[None, Unset, str]): Date of acknowledgment
        mitigated_at (Union[None, Unset, str]): Date of mitigation
        resolved_at (Union[None, Unset, str]): Date of resolution
        closed_at (Union[None, Unset, str]): Date of closure
        cancelled_at (Union[None, Unset, str]): Date of cancellation
    """

    title: str
    created_at: str
    updated_at: str
    id: Unset | str = UNSET
    sequential_id: Unset | int = UNSET
    kind: Unset | str = UNSET
    slug: Unset | str = UNSET
    parent_incident_id: None | Unset | str = UNSET
    duplicate_incident_id: None | Unset | str = UNSET
    summary: None | Unset | str = UNSET
    private: Unset | bool = False
    source: None | Unset | str = UNSET
    status: None | Unset | str = UNSET
    url: None | Unset | str = UNSET
    short_url: None | Unset | str = UNSET
    public_title: None | Unset | str = UNSET
    user: Union["IncidentUserType0", None, Unset] = UNSET
    severity: Union[Unset, "SeverityResponse"] = UNSET
    environments: None | Unset | list["EnvironmentResponse"] = UNSET
    incident_types: None | Unset | list["IncidentTypeResponse"] = UNSET
    services: None | Unset | list["ServiceResponse"] = UNSET
    functionalities: None | Unset | list["FunctionalityResponse"] = UNSET
    groups: None | Unset | list["TeamResponse"] = UNSET
    labels: Union["IncidentLabelsType0", None, Unset] = UNSET
    slack_channel_id: None | Unset | str = UNSET
    slack_channel_name: None | Unset | str = UNSET
    slack_channel_url: None | Unset | str = UNSET
    slack_channel_short_url: None | Unset | str = UNSET
    slack_channel_deep_link: None | Unset | str = UNSET
    slack_channel_archived: None | Unset | bool = UNSET
    slack_last_message_ts: None | Unset | str = UNSET
    zoom_meeting_id: None | Unset | str = UNSET
    zoom_meeting_start_url: None | Unset | str = UNSET
    zoom_meeting_join_url: None | Unset | str = UNSET
    zoom_meeting_password: None | Unset | str = UNSET
    zoom_meeting_pstn_password: None | Unset | str = UNSET
    zoom_meeting_h323_password: None | Unset | str = UNSET
    zoom_meeting_global_dial_in_numbers: None | Unset | list[str] = UNSET
    google_drive_id: None | Unset | str = UNSET
    google_drive_parent_id: None | Unset | str = UNSET
    google_drive_url: None | Unset | str = UNSET
    google_meeting_id: None | Unset | str = UNSET
    google_meeting_url: None | Unset | str = UNSET
    jira_issue_key: None | Unset | str = UNSET
    jira_issue_id: None | Unset | str = UNSET
    jira_issue_url: None | Unset | str = UNSET
    github_issue_id: None | Unset | str = UNSET
    github_issue_url: None | Unset | str = UNSET
    gitlab_issue_id: None | Unset | str = UNSET
    gitlab_issue_url: None | Unset | str = UNSET
    asana_task_id: None | Unset | str = UNSET
    asana_task_url: None | Unset | str = UNSET
    linear_issue_id: None | Unset | str = UNSET
    linear_issue_url: None | Unset | str = UNSET
    trello_card_id: None | Unset | str = UNSET
    trello_card_url: None | Unset | str = UNSET
    zendesk_ticket_id: None | Unset | str = UNSET
    zendesk_ticket_url: None | Unset | str = UNSET
    pagerduty_incident_id: None | Unset | str = UNSET
    pagerduty_incident_number: None | Unset | str = UNSET
    pagerduty_incident_url: None | Unset | str = UNSET
    opsgenie_incident_id: None | Unset | str = UNSET
    opsgenie_incident_url: None | Unset | str = UNSET
    opsgenie_alert_id: None | Unset | str = UNSET
    opsgenie_alert_url: None | Unset | str = UNSET
    service_now_incident_id: None | Unset | str = UNSET
    service_now_incident_key: None | Unset | str = UNSET
    service_now_incident_url: None | Unset | str = UNSET
    mattermost_channel_id: None | Unset | str = UNSET
    mattermost_channel_name: None | Unset | str = UNSET
    mattermost_channel_url: None | Unset | str = UNSET
    confluence_page_id: None | Unset | str = UNSET
    confluence_page_url: None | Unset | str = UNSET
    datadog_notebook_id: None | Unset | str = UNSET
    datadog_notebook_url: None | Unset | str = UNSET
    shortcut_story_id: None | Unset | str = UNSET
    shortcut_story_url: None | Unset | str = UNSET
    shortcut_task_id: None | Unset | str = UNSET
    shortcut_task_url: None | Unset | str = UNSET
    motion_task_id: None | Unset | str = UNSET
    motion_task_url: None | Unset | str = UNSET
    clickup_task_id: None | Unset | str = UNSET
    clickup_task_url: None | Unset | str = UNSET
    victor_ops_incident_id: None | Unset | str = UNSET
    victor_ops_incident_url: None | Unset | str = UNSET
    quip_page_id: None | Unset | str = UNSET
    quip_page_url: None | Unset | str = UNSET
    sharepoint_page_id: None | Unset | str = UNSET
    sharepoint_page_url: None | Unset | str = UNSET
    airtable_base_key: None | Unset | str = UNSET
    airtable_table_name: None | Unset | str = UNSET
    airtable_record_id: None | Unset | str = UNSET
    airtable_record_url: None | Unset | str = UNSET
    freshservice_ticket_id: None | Unset | str = UNSET
    freshservice_ticket_url: None | Unset | str = UNSET
    freshservice_task_id: None | Unset | str = UNSET
    freshservice_task_url: None | Unset | str = UNSET
    mitigation_message: None | Unset | str = UNSET
    resolution_message: None | Unset | str = UNSET
    cancellation_message: None | Unset | str = UNSET
    scheduled_for: None | Unset | str = UNSET
    scheduled_until: None | Unset | str = UNSET
    muted_service_ids: None | Unset | list[str] = UNSET
    retrospective_progress_status: Unset | IncidentRetrospectiveProgressStatus = UNSET
    in_triage_by: Union["IncidentInTriageByType0", None, Unset] = UNSET
    started_by: Union["IncidentStartedByType0", None, Unset] = UNSET
    mitigated_by: Union["IncidentMitigatedByType0", None, Unset] = UNSET
    resolved_by: Union["IncidentResolvedByType0", None, Unset] = UNSET
    closed_by: Union["IncidentClosedByType0", None, Unset] = UNSET
    cancelled_by: Union["IncidentCancelledByType0", None, Unset] = UNSET
    in_triage_at: None | Unset | str = UNSET
    started_at: None | Unset | str = UNSET
    detected_at: None | Unset | str = UNSET
    acknowledged_at: None | Unset | str = UNSET
    mitigated_at: None | Unset | str = UNSET
    resolved_at: None | Unset | str = UNSET
    closed_at: None | Unset | str = UNSET
    cancelled_at: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.incident_cancelled_by_type_0 import IncidentCancelledByType0
        from ..models.incident_closed_by_type_0 import IncidentClosedByType0
        from ..models.incident_in_triage_by_type_0 import IncidentInTriageByType0
        from ..models.incident_labels_type_0 import IncidentLabelsType0
        from ..models.incident_mitigated_by_type_0 import IncidentMitigatedByType0
        from ..models.incident_resolved_by_type_0 import IncidentResolvedByType0
        from ..models.incident_started_by_type_0 import IncidentStartedByType0
        from ..models.incident_user_type_0 import IncidentUserType0

        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        id = self.id

        sequential_id = self.sequential_id

        kind = self.kind

        slug = self.slug

        parent_incident_id: None | Unset | str
        if isinstance(self.parent_incident_id, Unset):
            parent_incident_id = UNSET
        else:
            parent_incident_id = self.parent_incident_id

        duplicate_incident_id: None | Unset | str
        if isinstance(self.duplicate_incident_id, Unset):
            duplicate_incident_id = UNSET
        else:
            duplicate_incident_id = self.duplicate_incident_id

        summary: None | Unset | str
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        private = self.private

        source: None | Unset | str
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        status: None | Unset | str
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        url: None | Unset | str
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        short_url: None | Unset | str
        if isinstance(self.short_url, Unset):
            short_url = UNSET
        else:
            short_url = self.short_url

        public_title: None | Unset | str
        if isinstance(self.public_title, Unset):
            public_title = UNSET
        else:
            public_title = self.public_title

        user: None | Unset | dict[str, Any]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, IncidentUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        severity: Unset | dict[str, Any] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        environments: None | Unset | list[dict[str, Any]]
        if isinstance(self.environments, Unset):
            environments = UNSET
        elif isinstance(self.environments, list):
            environments = []
            for environments_type_0_item_data in self.environments:
                environments_type_0_item = environments_type_0_item_data.to_dict()
                environments.append(environments_type_0_item)

        else:
            environments = self.environments

        incident_types: None | Unset | list[dict[str, Any]]
        if isinstance(self.incident_types, Unset):
            incident_types = UNSET
        elif isinstance(self.incident_types, list):
            incident_types = []
            for incident_types_type_0_item_data in self.incident_types:
                incident_types_type_0_item = incident_types_type_0_item_data.to_dict()
                incident_types.append(incident_types_type_0_item)

        else:
            incident_types = self.incident_types

        services: None | Unset | list[dict[str, Any]]
        if isinstance(self.services, Unset):
            services = UNSET
        elif isinstance(self.services, list):
            services = []
            for services_type_0_item_data in self.services:
                services_type_0_item = services_type_0_item_data.to_dict()
                services.append(services_type_0_item)

        else:
            services = self.services

        functionalities: None | Unset | list[dict[str, Any]]
        if isinstance(self.functionalities, Unset):
            functionalities = UNSET
        elif isinstance(self.functionalities, list):
            functionalities = []
            for functionalities_type_0_item_data in self.functionalities:
                functionalities_type_0_item = functionalities_type_0_item_data.to_dict()
                functionalities.append(functionalities_type_0_item)

        else:
            functionalities = self.functionalities

        groups: None | Unset | list[dict[str, Any]]
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        labels: None | Unset | dict[str, Any]
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, IncidentLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        slack_channel_id: None | Unset | str
        if isinstance(self.slack_channel_id, Unset):
            slack_channel_id = UNSET
        else:
            slack_channel_id = self.slack_channel_id

        slack_channel_name: None | Unset | str
        if isinstance(self.slack_channel_name, Unset):
            slack_channel_name = UNSET
        else:
            slack_channel_name = self.slack_channel_name

        slack_channel_url: None | Unset | str
        if isinstance(self.slack_channel_url, Unset):
            slack_channel_url = UNSET
        else:
            slack_channel_url = self.slack_channel_url

        slack_channel_short_url: None | Unset | str
        if isinstance(self.slack_channel_short_url, Unset):
            slack_channel_short_url = UNSET
        else:
            slack_channel_short_url = self.slack_channel_short_url

        slack_channel_deep_link: None | Unset | str
        if isinstance(self.slack_channel_deep_link, Unset):
            slack_channel_deep_link = UNSET
        else:
            slack_channel_deep_link = self.slack_channel_deep_link

        slack_channel_archived: None | Unset | bool
        if isinstance(self.slack_channel_archived, Unset):
            slack_channel_archived = UNSET
        else:
            slack_channel_archived = self.slack_channel_archived

        slack_last_message_ts: None | Unset | str
        if isinstance(self.slack_last_message_ts, Unset):
            slack_last_message_ts = UNSET
        else:
            slack_last_message_ts = self.slack_last_message_ts

        zoom_meeting_id: None | Unset | str
        if isinstance(self.zoom_meeting_id, Unset):
            zoom_meeting_id = UNSET
        else:
            zoom_meeting_id = self.zoom_meeting_id

        zoom_meeting_start_url: None | Unset | str
        if isinstance(self.zoom_meeting_start_url, Unset):
            zoom_meeting_start_url = UNSET
        else:
            zoom_meeting_start_url = self.zoom_meeting_start_url

        zoom_meeting_join_url: None | Unset | str
        if isinstance(self.zoom_meeting_join_url, Unset):
            zoom_meeting_join_url = UNSET
        else:
            zoom_meeting_join_url = self.zoom_meeting_join_url

        zoom_meeting_password: None | Unset | str
        if isinstance(self.zoom_meeting_password, Unset):
            zoom_meeting_password = UNSET
        else:
            zoom_meeting_password = self.zoom_meeting_password

        zoom_meeting_pstn_password: None | Unset | str
        if isinstance(self.zoom_meeting_pstn_password, Unset):
            zoom_meeting_pstn_password = UNSET
        else:
            zoom_meeting_pstn_password = self.zoom_meeting_pstn_password

        zoom_meeting_h323_password: None | Unset | str
        if isinstance(self.zoom_meeting_h323_password, Unset):
            zoom_meeting_h323_password = UNSET
        else:
            zoom_meeting_h323_password = self.zoom_meeting_h323_password

        zoom_meeting_global_dial_in_numbers: None | Unset | list[str]
        if isinstance(self.zoom_meeting_global_dial_in_numbers, Unset):
            zoom_meeting_global_dial_in_numbers = UNSET
        elif isinstance(self.zoom_meeting_global_dial_in_numbers, list):
            zoom_meeting_global_dial_in_numbers = self.zoom_meeting_global_dial_in_numbers

        else:
            zoom_meeting_global_dial_in_numbers = self.zoom_meeting_global_dial_in_numbers

        google_drive_id: None | Unset | str
        if isinstance(self.google_drive_id, Unset):
            google_drive_id = UNSET
        else:
            google_drive_id = self.google_drive_id

        google_drive_parent_id: None | Unset | str
        if isinstance(self.google_drive_parent_id, Unset):
            google_drive_parent_id = UNSET
        else:
            google_drive_parent_id = self.google_drive_parent_id

        google_drive_url: None | Unset | str
        if isinstance(self.google_drive_url, Unset):
            google_drive_url = UNSET
        else:
            google_drive_url = self.google_drive_url

        google_meeting_id: None | Unset | str
        if isinstance(self.google_meeting_id, Unset):
            google_meeting_id = UNSET
        else:
            google_meeting_id = self.google_meeting_id

        google_meeting_url: None | Unset | str
        if isinstance(self.google_meeting_url, Unset):
            google_meeting_url = UNSET
        else:
            google_meeting_url = self.google_meeting_url

        jira_issue_key: None | Unset | str
        if isinstance(self.jira_issue_key, Unset):
            jira_issue_key = UNSET
        else:
            jira_issue_key = self.jira_issue_key

        jira_issue_id: None | Unset | str
        if isinstance(self.jira_issue_id, Unset):
            jira_issue_id = UNSET
        else:
            jira_issue_id = self.jira_issue_id

        jira_issue_url: None | Unset | str
        if isinstance(self.jira_issue_url, Unset):
            jira_issue_url = UNSET
        else:
            jira_issue_url = self.jira_issue_url

        github_issue_id: None | Unset | str
        if isinstance(self.github_issue_id, Unset):
            github_issue_id = UNSET
        else:
            github_issue_id = self.github_issue_id

        github_issue_url: None | Unset | str
        if isinstance(self.github_issue_url, Unset):
            github_issue_url = UNSET
        else:
            github_issue_url = self.github_issue_url

        gitlab_issue_id: None | Unset | str
        if isinstance(self.gitlab_issue_id, Unset):
            gitlab_issue_id = UNSET
        else:
            gitlab_issue_id = self.gitlab_issue_id

        gitlab_issue_url: None | Unset | str
        if isinstance(self.gitlab_issue_url, Unset):
            gitlab_issue_url = UNSET
        else:
            gitlab_issue_url = self.gitlab_issue_url

        asana_task_id: None | Unset | str
        if isinstance(self.asana_task_id, Unset):
            asana_task_id = UNSET
        else:
            asana_task_id = self.asana_task_id

        asana_task_url: None | Unset | str
        if isinstance(self.asana_task_url, Unset):
            asana_task_url = UNSET
        else:
            asana_task_url = self.asana_task_url

        linear_issue_id: None | Unset | str
        if isinstance(self.linear_issue_id, Unset):
            linear_issue_id = UNSET
        else:
            linear_issue_id = self.linear_issue_id

        linear_issue_url: None | Unset | str
        if isinstance(self.linear_issue_url, Unset):
            linear_issue_url = UNSET
        else:
            linear_issue_url = self.linear_issue_url

        trello_card_id: None | Unset | str
        if isinstance(self.trello_card_id, Unset):
            trello_card_id = UNSET
        else:
            trello_card_id = self.trello_card_id

        trello_card_url: None | Unset | str
        if isinstance(self.trello_card_url, Unset):
            trello_card_url = UNSET
        else:
            trello_card_url = self.trello_card_url

        zendesk_ticket_id: None | Unset | str
        if isinstance(self.zendesk_ticket_id, Unset):
            zendesk_ticket_id = UNSET
        else:
            zendesk_ticket_id = self.zendesk_ticket_id

        zendesk_ticket_url: None | Unset | str
        if isinstance(self.zendesk_ticket_url, Unset):
            zendesk_ticket_url = UNSET
        else:
            zendesk_ticket_url = self.zendesk_ticket_url

        pagerduty_incident_id: None | Unset | str
        if isinstance(self.pagerduty_incident_id, Unset):
            pagerduty_incident_id = UNSET
        else:
            pagerduty_incident_id = self.pagerduty_incident_id

        pagerduty_incident_number: None | Unset | str
        if isinstance(self.pagerduty_incident_number, Unset):
            pagerduty_incident_number = UNSET
        else:
            pagerduty_incident_number = self.pagerduty_incident_number

        pagerduty_incident_url: None | Unset | str
        if isinstance(self.pagerduty_incident_url, Unset):
            pagerduty_incident_url = UNSET
        else:
            pagerduty_incident_url = self.pagerduty_incident_url

        opsgenie_incident_id: None | Unset | str
        if isinstance(self.opsgenie_incident_id, Unset):
            opsgenie_incident_id = UNSET
        else:
            opsgenie_incident_id = self.opsgenie_incident_id

        opsgenie_incident_url: None | Unset | str
        if isinstance(self.opsgenie_incident_url, Unset):
            opsgenie_incident_url = UNSET
        else:
            opsgenie_incident_url = self.opsgenie_incident_url

        opsgenie_alert_id: None | Unset | str
        if isinstance(self.opsgenie_alert_id, Unset):
            opsgenie_alert_id = UNSET
        else:
            opsgenie_alert_id = self.opsgenie_alert_id

        opsgenie_alert_url: None | Unset | str
        if isinstance(self.opsgenie_alert_url, Unset):
            opsgenie_alert_url = UNSET
        else:
            opsgenie_alert_url = self.opsgenie_alert_url

        service_now_incident_id: None | Unset | str
        if isinstance(self.service_now_incident_id, Unset):
            service_now_incident_id = UNSET
        else:
            service_now_incident_id = self.service_now_incident_id

        service_now_incident_key: None | Unset | str
        if isinstance(self.service_now_incident_key, Unset):
            service_now_incident_key = UNSET
        else:
            service_now_incident_key = self.service_now_incident_key

        service_now_incident_url: None | Unset | str
        if isinstance(self.service_now_incident_url, Unset):
            service_now_incident_url = UNSET
        else:
            service_now_incident_url = self.service_now_incident_url

        mattermost_channel_id: None | Unset | str
        if isinstance(self.mattermost_channel_id, Unset):
            mattermost_channel_id = UNSET
        else:
            mattermost_channel_id = self.mattermost_channel_id

        mattermost_channel_name: None | Unset | str
        if isinstance(self.mattermost_channel_name, Unset):
            mattermost_channel_name = UNSET
        else:
            mattermost_channel_name = self.mattermost_channel_name

        mattermost_channel_url: None | Unset | str
        if isinstance(self.mattermost_channel_url, Unset):
            mattermost_channel_url = UNSET
        else:
            mattermost_channel_url = self.mattermost_channel_url

        confluence_page_id: None | Unset | str
        if isinstance(self.confluence_page_id, Unset):
            confluence_page_id = UNSET
        else:
            confluence_page_id = self.confluence_page_id

        confluence_page_url: None | Unset | str
        if isinstance(self.confluence_page_url, Unset):
            confluence_page_url = UNSET
        else:
            confluence_page_url = self.confluence_page_url

        datadog_notebook_id: None | Unset | str
        if isinstance(self.datadog_notebook_id, Unset):
            datadog_notebook_id = UNSET
        else:
            datadog_notebook_id = self.datadog_notebook_id

        datadog_notebook_url: None | Unset | str
        if isinstance(self.datadog_notebook_url, Unset):
            datadog_notebook_url = UNSET
        else:
            datadog_notebook_url = self.datadog_notebook_url

        shortcut_story_id: None | Unset | str
        if isinstance(self.shortcut_story_id, Unset):
            shortcut_story_id = UNSET
        else:
            shortcut_story_id = self.shortcut_story_id

        shortcut_story_url: None | Unset | str
        if isinstance(self.shortcut_story_url, Unset):
            shortcut_story_url = UNSET
        else:
            shortcut_story_url = self.shortcut_story_url

        shortcut_task_id: None | Unset | str
        if isinstance(self.shortcut_task_id, Unset):
            shortcut_task_id = UNSET
        else:
            shortcut_task_id = self.shortcut_task_id

        shortcut_task_url: None | Unset | str
        if isinstance(self.shortcut_task_url, Unset):
            shortcut_task_url = UNSET
        else:
            shortcut_task_url = self.shortcut_task_url

        motion_task_id: None | Unset | str
        if isinstance(self.motion_task_id, Unset):
            motion_task_id = UNSET
        else:
            motion_task_id = self.motion_task_id

        motion_task_url: None | Unset | str
        if isinstance(self.motion_task_url, Unset):
            motion_task_url = UNSET
        else:
            motion_task_url = self.motion_task_url

        clickup_task_id: None | Unset | str
        if isinstance(self.clickup_task_id, Unset):
            clickup_task_id = UNSET
        else:
            clickup_task_id = self.clickup_task_id

        clickup_task_url: None | Unset | str
        if isinstance(self.clickup_task_url, Unset):
            clickup_task_url = UNSET
        else:
            clickup_task_url = self.clickup_task_url

        victor_ops_incident_id: None | Unset | str
        if isinstance(self.victor_ops_incident_id, Unset):
            victor_ops_incident_id = UNSET
        else:
            victor_ops_incident_id = self.victor_ops_incident_id

        victor_ops_incident_url: None | Unset | str
        if isinstance(self.victor_ops_incident_url, Unset):
            victor_ops_incident_url = UNSET
        else:
            victor_ops_incident_url = self.victor_ops_incident_url

        quip_page_id: None | Unset | str
        if isinstance(self.quip_page_id, Unset):
            quip_page_id = UNSET
        else:
            quip_page_id = self.quip_page_id

        quip_page_url: None | Unset | str
        if isinstance(self.quip_page_url, Unset):
            quip_page_url = UNSET
        else:
            quip_page_url = self.quip_page_url

        sharepoint_page_id: None | Unset | str
        if isinstance(self.sharepoint_page_id, Unset):
            sharepoint_page_id = UNSET
        else:
            sharepoint_page_id = self.sharepoint_page_id

        sharepoint_page_url: None | Unset | str
        if isinstance(self.sharepoint_page_url, Unset):
            sharepoint_page_url = UNSET
        else:
            sharepoint_page_url = self.sharepoint_page_url

        airtable_base_key: None | Unset | str
        if isinstance(self.airtable_base_key, Unset):
            airtable_base_key = UNSET
        else:
            airtable_base_key = self.airtable_base_key

        airtable_table_name: None | Unset | str
        if isinstance(self.airtable_table_name, Unset):
            airtable_table_name = UNSET
        else:
            airtable_table_name = self.airtable_table_name

        airtable_record_id: None | Unset | str
        if isinstance(self.airtable_record_id, Unset):
            airtable_record_id = UNSET
        else:
            airtable_record_id = self.airtable_record_id

        airtable_record_url: None | Unset | str
        if isinstance(self.airtable_record_url, Unset):
            airtable_record_url = UNSET
        else:
            airtable_record_url = self.airtable_record_url

        freshservice_ticket_id: None | Unset | str
        if isinstance(self.freshservice_ticket_id, Unset):
            freshservice_ticket_id = UNSET
        else:
            freshservice_ticket_id = self.freshservice_ticket_id

        freshservice_ticket_url: None | Unset | str
        if isinstance(self.freshservice_ticket_url, Unset):
            freshservice_ticket_url = UNSET
        else:
            freshservice_ticket_url = self.freshservice_ticket_url

        freshservice_task_id: None | Unset | str
        if isinstance(self.freshservice_task_id, Unset):
            freshservice_task_id = UNSET
        else:
            freshservice_task_id = self.freshservice_task_id

        freshservice_task_url: None | Unset | str
        if isinstance(self.freshservice_task_url, Unset):
            freshservice_task_url = UNSET
        else:
            freshservice_task_url = self.freshservice_task_url

        mitigation_message: None | Unset | str
        if isinstance(self.mitigation_message, Unset):
            mitigation_message = UNSET
        else:
            mitigation_message = self.mitigation_message

        resolution_message: None | Unset | str
        if isinstance(self.resolution_message, Unset):
            resolution_message = UNSET
        else:
            resolution_message = self.resolution_message

        cancellation_message: None | Unset | str
        if isinstance(self.cancellation_message, Unset):
            cancellation_message = UNSET
        else:
            cancellation_message = self.cancellation_message

        scheduled_for: None | Unset | str
        if isinstance(self.scheduled_for, Unset):
            scheduled_for = UNSET
        else:
            scheduled_for = self.scheduled_for

        scheduled_until: None | Unset | str
        if isinstance(self.scheduled_until, Unset):
            scheduled_until = UNSET
        else:
            scheduled_until = self.scheduled_until

        muted_service_ids: None | Unset | list[str]
        if isinstance(self.muted_service_ids, Unset):
            muted_service_ids = UNSET
        elif isinstance(self.muted_service_ids, list):
            muted_service_ids = self.muted_service_ids

        else:
            muted_service_ids = self.muted_service_ids

        retrospective_progress_status: Unset | str = UNSET
        if not isinstance(self.retrospective_progress_status, Unset):
            retrospective_progress_status = self.retrospective_progress_status

        in_triage_by: None | Unset | dict[str, Any]
        if isinstance(self.in_triage_by, Unset):
            in_triage_by = UNSET
        elif isinstance(self.in_triage_by, IncidentInTriageByType0):
            in_triage_by = self.in_triage_by.to_dict()
        else:
            in_triage_by = self.in_triage_by

        started_by: None | Unset | dict[str, Any]
        if isinstance(self.started_by, Unset):
            started_by = UNSET
        elif isinstance(self.started_by, IncidentStartedByType0):
            started_by = self.started_by.to_dict()
        else:
            started_by = self.started_by

        mitigated_by: None | Unset | dict[str, Any]
        if isinstance(self.mitigated_by, Unset):
            mitigated_by = UNSET
        elif isinstance(self.mitigated_by, IncidentMitigatedByType0):
            mitigated_by = self.mitigated_by.to_dict()
        else:
            mitigated_by = self.mitigated_by

        resolved_by: None | Unset | dict[str, Any]
        if isinstance(self.resolved_by, Unset):
            resolved_by = UNSET
        elif isinstance(self.resolved_by, IncidentResolvedByType0):
            resolved_by = self.resolved_by.to_dict()
        else:
            resolved_by = self.resolved_by

        closed_by: None | Unset | dict[str, Any]
        if isinstance(self.closed_by, Unset):
            closed_by = UNSET
        elif isinstance(self.closed_by, IncidentClosedByType0):
            closed_by = self.closed_by.to_dict()
        else:
            closed_by = self.closed_by

        cancelled_by: None | Unset | dict[str, Any]
        if isinstance(self.cancelled_by, Unset):
            cancelled_by = UNSET
        elif isinstance(self.cancelled_by, IncidentCancelledByType0):
            cancelled_by = self.cancelled_by.to_dict()
        else:
            cancelled_by = self.cancelled_by

        in_triage_at: None | Unset | str
        if isinstance(self.in_triage_at, Unset):
            in_triage_at = UNSET
        else:
            in_triage_at = self.in_triage_at

        started_at: None | Unset | str
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        detected_at: None | Unset | str
        if isinstance(self.detected_at, Unset):
            detected_at = UNSET
        else:
            detected_at = self.detected_at

        acknowledged_at: None | Unset | str
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        mitigated_at: None | Unset | str
        if isinstance(self.mitigated_at, Unset):
            mitigated_at = UNSET
        else:
            mitigated_at = self.mitigated_at

        resolved_at: None | Unset | str
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        closed_at: None | Unset | str
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = self.closed_at

        cancelled_at: None | Unset | str
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = self.cancelled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if sequential_id is not UNSET:
            field_dict["sequential_id"] = sequential_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if slug is not UNSET:
            field_dict["slug"] = slug
        if parent_incident_id is not UNSET:
            field_dict["parent_incident_id"] = parent_incident_id
        if duplicate_incident_id is not UNSET:
            field_dict["duplicate_incident_id"] = duplicate_incident_id
        if summary is not UNSET:
            field_dict["summary"] = summary
        if private is not UNSET:
            field_dict["private"] = private
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if short_url is not UNSET:
            field_dict["short_url"] = short_url
        if public_title is not UNSET:
            field_dict["public_title"] = public_title
        if user is not UNSET:
            field_dict["user"] = user
        if severity is not UNSET:
            field_dict["severity"] = severity
        if environments is not UNSET:
            field_dict["environments"] = environments
        if incident_types is not UNSET:
            field_dict["incident_types"] = incident_types
        if services is not UNSET:
            field_dict["services"] = services
        if functionalities is not UNSET:
            field_dict["functionalities"] = functionalities
        if groups is not UNSET:
            field_dict["groups"] = groups
        if labels is not UNSET:
            field_dict["labels"] = labels
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
        if slack_channel_url is not UNSET:
            field_dict["slack_channel_url"] = slack_channel_url
        if slack_channel_short_url is not UNSET:
            field_dict["slack_channel_short_url"] = slack_channel_short_url
        if slack_channel_deep_link is not UNSET:
            field_dict["slack_channel_deep_link"] = slack_channel_deep_link
        if slack_channel_archived is not UNSET:
            field_dict["slack_channel_archived"] = slack_channel_archived
        if slack_last_message_ts is not UNSET:
            field_dict["slack_last_message_ts"] = slack_last_message_ts
        if zoom_meeting_id is not UNSET:
            field_dict["zoom_meeting_id"] = zoom_meeting_id
        if zoom_meeting_start_url is not UNSET:
            field_dict["zoom_meeting_start_url"] = zoom_meeting_start_url
        if zoom_meeting_join_url is not UNSET:
            field_dict["zoom_meeting_join_url"] = zoom_meeting_join_url
        if zoom_meeting_password is not UNSET:
            field_dict["zoom_meeting_password"] = zoom_meeting_password
        if zoom_meeting_pstn_password is not UNSET:
            field_dict["zoom_meeting_pstn_password"] = zoom_meeting_pstn_password
        if zoom_meeting_h323_password is not UNSET:
            field_dict["zoom_meeting_h323_password"] = zoom_meeting_h323_password
        if zoom_meeting_global_dial_in_numbers is not UNSET:
            field_dict["zoom_meeting_global_dial_in_numbers"] = zoom_meeting_global_dial_in_numbers
        if google_drive_id is not UNSET:
            field_dict["google_drive_id"] = google_drive_id
        if google_drive_parent_id is not UNSET:
            field_dict["google_drive_parent_id"] = google_drive_parent_id
        if google_drive_url is not UNSET:
            field_dict["google_drive_url"] = google_drive_url
        if google_meeting_id is not UNSET:
            field_dict["google_meeting_id"] = google_meeting_id
        if google_meeting_url is not UNSET:
            field_dict["google_meeting_url"] = google_meeting_url
        if jira_issue_key is not UNSET:
            field_dict["jira_issue_key"] = jira_issue_key
        if jira_issue_id is not UNSET:
            field_dict["jira_issue_id"] = jira_issue_id
        if jira_issue_url is not UNSET:
            field_dict["jira_issue_url"] = jira_issue_url
        if github_issue_id is not UNSET:
            field_dict["github_issue_id"] = github_issue_id
        if github_issue_url is not UNSET:
            field_dict["github_issue_url"] = github_issue_url
        if gitlab_issue_id is not UNSET:
            field_dict["gitlab_issue_id"] = gitlab_issue_id
        if gitlab_issue_url is not UNSET:
            field_dict["gitlab_issue_url"] = gitlab_issue_url
        if asana_task_id is not UNSET:
            field_dict["asana_task_id"] = asana_task_id
        if asana_task_url is not UNSET:
            field_dict["asana_task_url"] = asana_task_url
        if linear_issue_id is not UNSET:
            field_dict["linear_issue_id"] = linear_issue_id
        if linear_issue_url is not UNSET:
            field_dict["linear_issue_url"] = linear_issue_url
        if trello_card_id is not UNSET:
            field_dict["trello_card_id"] = trello_card_id
        if trello_card_url is not UNSET:
            field_dict["trello_card_url"] = trello_card_url
        if zendesk_ticket_id is not UNSET:
            field_dict["zendesk_ticket_id"] = zendesk_ticket_id
        if zendesk_ticket_url is not UNSET:
            field_dict["zendesk_ticket_url"] = zendesk_ticket_url
        if pagerduty_incident_id is not UNSET:
            field_dict["pagerduty_incident_id"] = pagerduty_incident_id
        if pagerduty_incident_number is not UNSET:
            field_dict["pagerduty_incident_number"] = pagerduty_incident_number
        if pagerduty_incident_url is not UNSET:
            field_dict["pagerduty_incident_url"] = pagerduty_incident_url
        if opsgenie_incident_id is not UNSET:
            field_dict["opsgenie_incident_id"] = opsgenie_incident_id
        if opsgenie_incident_url is not UNSET:
            field_dict["opsgenie_incident_url"] = opsgenie_incident_url
        if opsgenie_alert_id is not UNSET:
            field_dict["opsgenie_alert_id"] = opsgenie_alert_id
        if opsgenie_alert_url is not UNSET:
            field_dict["opsgenie_alert_url"] = opsgenie_alert_url
        if service_now_incident_id is not UNSET:
            field_dict["service_now_incident_id"] = service_now_incident_id
        if service_now_incident_key is not UNSET:
            field_dict["service_now_incident_key"] = service_now_incident_key
        if service_now_incident_url is not UNSET:
            field_dict["service_now_incident_url"] = service_now_incident_url
        if mattermost_channel_id is not UNSET:
            field_dict["mattermost_channel_id"] = mattermost_channel_id
        if mattermost_channel_name is not UNSET:
            field_dict["mattermost_channel_name"] = mattermost_channel_name
        if mattermost_channel_url is not UNSET:
            field_dict["mattermost_channel_url"] = mattermost_channel_url
        if confluence_page_id is not UNSET:
            field_dict["confluence_page_id"] = confluence_page_id
        if confluence_page_url is not UNSET:
            field_dict["confluence_page_url"] = confluence_page_url
        if datadog_notebook_id is not UNSET:
            field_dict["datadog_notebook_id"] = datadog_notebook_id
        if datadog_notebook_url is not UNSET:
            field_dict["datadog_notebook_url"] = datadog_notebook_url
        if shortcut_story_id is not UNSET:
            field_dict["shortcut_story_id"] = shortcut_story_id
        if shortcut_story_url is not UNSET:
            field_dict["shortcut_story_url"] = shortcut_story_url
        if shortcut_task_id is not UNSET:
            field_dict["shortcut_task_id"] = shortcut_task_id
        if shortcut_task_url is not UNSET:
            field_dict["shortcut_task_url"] = shortcut_task_url
        if motion_task_id is not UNSET:
            field_dict["motion_task_id"] = motion_task_id
        if motion_task_url is not UNSET:
            field_dict["motion_task_url"] = motion_task_url
        if clickup_task_id is not UNSET:
            field_dict["clickup_task_id"] = clickup_task_id
        if clickup_task_url is not UNSET:
            field_dict["clickup_task_url"] = clickup_task_url
        if victor_ops_incident_id is not UNSET:
            field_dict["victor_ops_incident_id"] = victor_ops_incident_id
        if victor_ops_incident_url is not UNSET:
            field_dict["victor_ops_incident_url"] = victor_ops_incident_url
        if quip_page_id is not UNSET:
            field_dict["quip_page_id"] = quip_page_id
        if quip_page_url is not UNSET:
            field_dict["quip_page_url"] = quip_page_url
        if sharepoint_page_id is not UNSET:
            field_dict["sharepoint_page_id"] = sharepoint_page_id
        if sharepoint_page_url is not UNSET:
            field_dict["sharepoint_page_url"] = sharepoint_page_url
        if airtable_base_key is not UNSET:
            field_dict["airtable_base_key"] = airtable_base_key
        if airtable_table_name is not UNSET:
            field_dict["airtable_table_name"] = airtable_table_name
        if airtable_record_id is not UNSET:
            field_dict["airtable_record_id"] = airtable_record_id
        if airtable_record_url is not UNSET:
            field_dict["airtable_record_url"] = airtable_record_url
        if freshservice_ticket_id is not UNSET:
            field_dict["freshservice_ticket_id"] = freshservice_ticket_id
        if freshservice_ticket_url is not UNSET:
            field_dict["freshservice_ticket_url"] = freshservice_ticket_url
        if freshservice_task_id is not UNSET:
            field_dict["freshservice_task_id"] = freshservice_task_id
        if freshservice_task_url is not UNSET:
            field_dict["freshservice_task_url"] = freshservice_task_url
        if mitigation_message is not UNSET:
            field_dict["mitigation_message"] = mitigation_message
        if resolution_message is not UNSET:
            field_dict["resolution_message"] = resolution_message
        if cancellation_message is not UNSET:
            field_dict["cancellation_message"] = cancellation_message
        if scheduled_for is not UNSET:
            field_dict["scheduled_for"] = scheduled_for
        if scheduled_until is not UNSET:
            field_dict["scheduled_until"] = scheduled_until
        if muted_service_ids is not UNSET:
            field_dict["muted_service_ids"] = muted_service_ids
        if retrospective_progress_status is not UNSET:
            field_dict["retrospective_progress_status"] = retrospective_progress_status
        if in_triage_by is not UNSET:
            field_dict["in_triage_by"] = in_triage_by
        if started_by is not UNSET:
            field_dict["started_by"] = started_by
        if mitigated_by is not UNSET:
            field_dict["mitigated_by"] = mitigated_by
        if resolved_by is not UNSET:
            field_dict["resolved_by"] = resolved_by
        if closed_by is not UNSET:
            field_dict["closed_by"] = closed_by
        if cancelled_by is not UNSET:
            field_dict["cancelled_by"] = cancelled_by
        if in_triage_at is not UNSET:
            field_dict["in_triage_at"] = in_triage_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if detected_at is not UNSET:
            field_dict["detected_at"] = detected_at
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if mitigated_at is not UNSET:
            field_dict["mitigated_at"] = mitigated_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_response import EnvironmentResponse
        from ..models.functionality_response import FunctionalityResponse
        from ..models.incident_cancelled_by_type_0 import IncidentCancelledByType0
        from ..models.incident_closed_by_type_0 import IncidentClosedByType0
        from ..models.incident_in_triage_by_type_0 import IncidentInTriageByType0
        from ..models.incident_labels_type_0 import IncidentLabelsType0
        from ..models.incident_mitigated_by_type_0 import IncidentMitigatedByType0
        from ..models.incident_resolved_by_type_0 import IncidentResolvedByType0
        from ..models.incident_started_by_type_0 import IncidentStartedByType0
        from ..models.incident_type_response import IncidentTypeResponse
        from ..models.incident_user_type_0 import IncidentUserType0
        from ..models.service_response import ServiceResponse
        from ..models.severity_response import SeverityResponse
        from ..models.team_response import TeamResponse

        d = dict(src_dict)
        title = d.pop("title")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        id = d.pop("id", UNSET)

        sequential_id = d.pop("sequential_id", UNSET)

        kind = d.pop("kind", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_parent_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        parent_incident_id = _parse_parent_incident_id(d.pop("parent_incident_id", UNSET))

        def _parse_duplicate_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        duplicate_incident_id = _parse_duplicate_incident_id(d.pop("duplicate_incident_id", UNSET))

        def _parse_summary(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        private = d.pop("private", UNSET)

        def _parse_source(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_status(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_short_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        short_url = _parse_short_url(d.pop("short_url", UNSET))

        def _parse_public_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        public_title = _parse_public_title(d.pop("public_title", UNSET))

        def _parse_user(data: object) -> Union["IncidentUserType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = IncidentUserType0.from_dict(data)

                return user_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentUserType0", None, Unset], data)

        user = _parse_user(d.pop("user", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: Unset | SeverityResponse
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityResponse.from_dict(_severity)

        def _parse_environments(data: object) -> None | Unset | list["EnvironmentResponse"]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environments_type_0 = []
                _environments_type_0 = data
                for environments_type_0_item_data in _environments_type_0:
                    environments_type_0_item = EnvironmentResponse.from_dict(environments_type_0_item_data)

                    environments_type_0.append(environments_type_0_item)

                return environments_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["EnvironmentResponse"], data)

        environments = _parse_environments(d.pop("environments", UNSET))

        def _parse_incident_types(data: object) -> None | Unset | list["IncidentTypeResponse"]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_types_type_0 = []
                _incident_types_type_0 = data
                for incident_types_type_0_item_data in _incident_types_type_0:
                    incident_types_type_0_item = IncidentTypeResponse.from_dict(incident_types_type_0_item_data)

                    incident_types_type_0.append(incident_types_type_0_item)

                return incident_types_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["IncidentTypeResponse"], data)

        incident_types = _parse_incident_types(d.pop("incident_types", UNSET))

        def _parse_services(data: object) -> None | Unset | list["ServiceResponse"]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                services_type_0 = []
                _services_type_0 = data
                for services_type_0_item_data in _services_type_0:
                    services_type_0_item = ServiceResponse.from_dict(services_type_0_item_data)

                    services_type_0.append(services_type_0_item)

                return services_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["ServiceResponse"], data)

        services = _parse_services(d.pop("services", UNSET))

        def _parse_functionalities(data: object) -> None | Unset | list["FunctionalityResponse"]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionalities_type_0 = []
                _functionalities_type_0 = data
                for functionalities_type_0_item_data in _functionalities_type_0:
                    functionalities_type_0_item = FunctionalityResponse.from_dict(functionalities_type_0_item_data)

                    functionalities_type_0.append(functionalities_type_0_item)

                return functionalities_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["FunctionalityResponse"], data)

        functionalities = _parse_functionalities(d.pop("functionalities", UNSET))

        def _parse_groups(data: object) -> None | Unset | list["TeamResponse"]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = TeamResponse.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["TeamResponse"], data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_labels(data: object) -> Union["IncidentLabelsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = IncidentLabelsType0.from_dict(data)

                return labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentLabelsType0", None, Unset], data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_slack_channel_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_id = _parse_slack_channel_id(d.pop("slack_channel_id", UNSET))

        def _parse_slack_channel_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_name = _parse_slack_channel_name(d.pop("slack_channel_name", UNSET))

        def _parse_slack_channel_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_url = _parse_slack_channel_url(d.pop("slack_channel_url", UNSET))

        def _parse_slack_channel_short_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_short_url = _parse_slack_channel_short_url(d.pop("slack_channel_short_url", UNSET))

        def _parse_slack_channel_deep_link(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_deep_link = _parse_slack_channel_deep_link(d.pop("slack_channel_deep_link", UNSET))

        def _parse_slack_channel_archived(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        slack_channel_archived = _parse_slack_channel_archived(d.pop("slack_channel_archived", UNSET))

        def _parse_slack_last_message_ts(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_last_message_ts = _parse_slack_last_message_ts(d.pop("slack_last_message_ts", UNSET))

        def _parse_zoom_meeting_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zoom_meeting_id = _parse_zoom_meeting_id(d.pop("zoom_meeting_id", UNSET))

        def _parse_zoom_meeting_start_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zoom_meeting_start_url = _parse_zoom_meeting_start_url(d.pop("zoom_meeting_start_url", UNSET))

        def _parse_zoom_meeting_join_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zoom_meeting_join_url = _parse_zoom_meeting_join_url(d.pop("zoom_meeting_join_url", UNSET))

        def _parse_zoom_meeting_password(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zoom_meeting_password = _parse_zoom_meeting_password(d.pop("zoom_meeting_password", UNSET))

        def _parse_zoom_meeting_pstn_password(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zoom_meeting_pstn_password = _parse_zoom_meeting_pstn_password(d.pop("zoom_meeting_pstn_password", UNSET))

        def _parse_zoom_meeting_h323_password(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zoom_meeting_h323_password = _parse_zoom_meeting_h323_password(d.pop("zoom_meeting_h323_password", UNSET))

        def _parse_zoom_meeting_global_dial_in_numbers(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                zoom_meeting_global_dial_in_numbers_type_0 = cast(list[str], data)

                return zoom_meeting_global_dial_in_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        zoom_meeting_global_dial_in_numbers = _parse_zoom_meeting_global_dial_in_numbers(
            d.pop("zoom_meeting_global_dial_in_numbers", UNSET)
        )

        def _parse_google_drive_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        google_drive_id = _parse_google_drive_id(d.pop("google_drive_id", UNSET))

        def _parse_google_drive_parent_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        google_drive_parent_id = _parse_google_drive_parent_id(d.pop("google_drive_parent_id", UNSET))

        def _parse_google_drive_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        google_drive_url = _parse_google_drive_url(d.pop("google_drive_url", UNSET))

        def _parse_google_meeting_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        google_meeting_id = _parse_google_meeting_id(d.pop("google_meeting_id", UNSET))

        def _parse_google_meeting_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        google_meeting_url = _parse_google_meeting_url(d.pop("google_meeting_url", UNSET))

        def _parse_jira_issue_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_key = _parse_jira_issue_key(d.pop("jira_issue_key", UNSET))

        def _parse_jira_issue_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_id = _parse_jira_issue_id(d.pop("jira_issue_id", UNSET))

        def _parse_jira_issue_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_url = _parse_jira_issue_url(d.pop("jira_issue_url", UNSET))

        def _parse_github_issue_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        github_issue_id = _parse_github_issue_id(d.pop("github_issue_id", UNSET))

        def _parse_github_issue_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        github_issue_url = _parse_github_issue_url(d.pop("github_issue_url", UNSET))

        def _parse_gitlab_issue_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        gitlab_issue_id = _parse_gitlab_issue_id(d.pop("gitlab_issue_id", UNSET))

        def _parse_gitlab_issue_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        gitlab_issue_url = _parse_gitlab_issue_url(d.pop("gitlab_issue_url", UNSET))

        def _parse_asana_task_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        asana_task_id = _parse_asana_task_id(d.pop("asana_task_id", UNSET))

        def _parse_asana_task_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        asana_task_url = _parse_asana_task_url(d.pop("asana_task_url", UNSET))

        def _parse_linear_issue_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        linear_issue_id = _parse_linear_issue_id(d.pop("linear_issue_id", UNSET))

        def _parse_linear_issue_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        linear_issue_url = _parse_linear_issue_url(d.pop("linear_issue_url", UNSET))

        def _parse_trello_card_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        trello_card_id = _parse_trello_card_id(d.pop("trello_card_id", UNSET))

        def _parse_trello_card_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        trello_card_url = _parse_trello_card_url(d.pop("trello_card_url", UNSET))

        def _parse_zendesk_ticket_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zendesk_ticket_id = _parse_zendesk_ticket_id(d.pop("zendesk_ticket_id", UNSET))

        def _parse_zendesk_ticket_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        zendesk_ticket_url = _parse_zendesk_ticket_url(d.pop("zendesk_ticket_url", UNSET))

        def _parse_pagerduty_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pagerduty_incident_id = _parse_pagerduty_incident_id(d.pop("pagerduty_incident_id", UNSET))

        def _parse_pagerduty_incident_number(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pagerduty_incident_number = _parse_pagerduty_incident_number(d.pop("pagerduty_incident_number", UNSET))

        def _parse_pagerduty_incident_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pagerduty_incident_url = _parse_pagerduty_incident_url(d.pop("pagerduty_incident_url", UNSET))

        def _parse_opsgenie_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        opsgenie_incident_id = _parse_opsgenie_incident_id(d.pop("opsgenie_incident_id", UNSET))

        def _parse_opsgenie_incident_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        opsgenie_incident_url = _parse_opsgenie_incident_url(d.pop("opsgenie_incident_url", UNSET))

        def _parse_opsgenie_alert_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        opsgenie_alert_id = _parse_opsgenie_alert_id(d.pop("opsgenie_alert_id", UNSET))

        def _parse_opsgenie_alert_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        opsgenie_alert_url = _parse_opsgenie_alert_url(d.pop("opsgenie_alert_url", UNSET))

        def _parse_service_now_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        service_now_incident_id = _parse_service_now_incident_id(d.pop("service_now_incident_id", UNSET))

        def _parse_service_now_incident_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        service_now_incident_key = _parse_service_now_incident_key(d.pop("service_now_incident_key", UNSET))

        def _parse_service_now_incident_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        service_now_incident_url = _parse_service_now_incident_url(d.pop("service_now_incident_url", UNSET))

        def _parse_mattermost_channel_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mattermost_channel_id = _parse_mattermost_channel_id(d.pop("mattermost_channel_id", UNSET))

        def _parse_mattermost_channel_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mattermost_channel_name = _parse_mattermost_channel_name(d.pop("mattermost_channel_name", UNSET))

        def _parse_mattermost_channel_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mattermost_channel_url = _parse_mattermost_channel_url(d.pop("mattermost_channel_url", UNSET))

        def _parse_confluence_page_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        confluence_page_id = _parse_confluence_page_id(d.pop("confluence_page_id", UNSET))

        def _parse_confluence_page_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        confluence_page_url = _parse_confluence_page_url(d.pop("confluence_page_url", UNSET))

        def _parse_datadog_notebook_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        datadog_notebook_id = _parse_datadog_notebook_id(d.pop("datadog_notebook_id", UNSET))

        def _parse_datadog_notebook_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        datadog_notebook_url = _parse_datadog_notebook_url(d.pop("datadog_notebook_url", UNSET))

        def _parse_shortcut_story_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        shortcut_story_id = _parse_shortcut_story_id(d.pop("shortcut_story_id", UNSET))

        def _parse_shortcut_story_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        shortcut_story_url = _parse_shortcut_story_url(d.pop("shortcut_story_url", UNSET))

        def _parse_shortcut_task_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        shortcut_task_id = _parse_shortcut_task_id(d.pop("shortcut_task_id", UNSET))

        def _parse_shortcut_task_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        shortcut_task_url = _parse_shortcut_task_url(d.pop("shortcut_task_url", UNSET))

        def _parse_motion_task_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        motion_task_id = _parse_motion_task_id(d.pop("motion_task_id", UNSET))

        def _parse_motion_task_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        motion_task_url = _parse_motion_task_url(d.pop("motion_task_url", UNSET))

        def _parse_clickup_task_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        clickup_task_id = _parse_clickup_task_id(d.pop("clickup_task_id", UNSET))

        def _parse_clickup_task_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        clickup_task_url = _parse_clickup_task_url(d.pop("clickup_task_url", UNSET))

        def _parse_victor_ops_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        victor_ops_incident_id = _parse_victor_ops_incident_id(d.pop("victor_ops_incident_id", UNSET))

        def _parse_victor_ops_incident_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        victor_ops_incident_url = _parse_victor_ops_incident_url(d.pop("victor_ops_incident_url", UNSET))

        def _parse_quip_page_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        quip_page_id = _parse_quip_page_id(d.pop("quip_page_id", UNSET))

        def _parse_quip_page_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        quip_page_url = _parse_quip_page_url(d.pop("quip_page_url", UNSET))

        def _parse_sharepoint_page_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        sharepoint_page_id = _parse_sharepoint_page_id(d.pop("sharepoint_page_id", UNSET))

        def _parse_sharepoint_page_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        sharepoint_page_url = _parse_sharepoint_page_url(d.pop("sharepoint_page_url", UNSET))

        def _parse_airtable_base_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        airtable_base_key = _parse_airtable_base_key(d.pop("airtable_base_key", UNSET))

        def _parse_airtable_table_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        airtable_table_name = _parse_airtable_table_name(d.pop("airtable_table_name", UNSET))

        def _parse_airtable_record_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        airtable_record_id = _parse_airtable_record_id(d.pop("airtable_record_id", UNSET))

        def _parse_airtable_record_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        airtable_record_url = _parse_airtable_record_url(d.pop("airtable_record_url", UNSET))

        def _parse_freshservice_ticket_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        freshservice_ticket_id = _parse_freshservice_ticket_id(d.pop("freshservice_ticket_id", UNSET))

        def _parse_freshservice_ticket_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        freshservice_ticket_url = _parse_freshservice_ticket_url(d.pop("freshservice_ticket_url", UNSET))

        def _parse_freshservice_task_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        freshservice_task_id = _parse_freshservice_task_id(d.pop("freshservice_task_id", UNSET))

        def _parse_freshservice_task_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        freshservice_task_url = _parse_freshservice_task_url(d.pop("freshservice_task_url", UNSET))

        def _parse_mitigation_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mitigation_message = _parse_mitigation_message(d.pop("mitigation_message", UNSET))

        def _parse_resolution_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        resolution_message = _parse_resolution_message(d.pop("resolution_message", UNSET))

        def _parse_cancellation_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        cancellation_message = _parse_cancellation_message(d.pop("cancellation_message", UNSET))

        def _parse_scheduled_for(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        scheduled_for = _parse_scheduled_for(d.pop("scheduled_for", UNSET))

        def _parse_scheduled_until(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        scheduled_until = _parse_scheduled_until(d.pop("scheduled_until", UNSET))

        def _parse_muted_service_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                muted_service_ids_type_0 = cast(list[str], data)

                return muted_service_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        muted_service_ids = _parse_muted_service_ids(d.pop("muted_service_ids", UNSET))

        _retrospective_progress_status = d.pop("retrospective_progress_status", UNSET)
        retrospective_progress_status: Unset | IncidentRetrospectiveProgressStatus
        if isinstance(_retrospective_progress_status, Unset):
            retrospective_progress_status = UNSET
        else:
            retrospective_progress_status = check_incident_retrospective_progress_status(_retrospective_progress_status)

        def _parse_in_triage_by(data: object) -> Union["IncidentInTriageByType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                in_triage_by_type_0 = IncidentInTriageByType0.from_dict(data)

                return in_triage_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentInTriageByType0", None, Unset], data)

        in_triage_by = _parse_in_triage_by(d.pop("in_triage_by", UNSET))

        def _parse_started_by(data: object) -> Union["IncidentStartedByType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                started_by_type_0 = IncidentStartedByType0.from_dict(data)

                return started_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentStartedByType0", None, Unset], data)

        started_by = _parse_started_by(d.pop("started_by", UNSET))

        def _parse_mitigated_by(data: object) -> Union["IncidentMitigatedByType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mitigated_by_type_0 = IncidentMitigatedByType0.from_dict(data)

                return mitigated_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentMitigatedByType0", None, Unset], data)

        mitigated_by = _parse_mitigated_by(d.pop("mitigated_by", UNSET))

        def _parse_resolved_by(data: object) -> Union["IncidentResolvedByType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolved_by_type_0 = IncidentResolvedByType0.from_dict(data)

                return resolved_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentResolvedByType0", None, Unset], data)

        resolved_by = _parse_resolved_by(d.pop("resolved_by", UNSET))

        def _parse_closed_by(data: object) -> Union["IncidentClosedByType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                closed_by_type_0 = IncidentClosedByType0.from_dict(data)

                return closed_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentClosedByType0", None, Unset], data)

        closed_by = _parse_closed_by(d.pop("closed_by", UNSET))

        def _parse_cancelled_by(data: object) -> Union["IncidentCancelledByType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cancelled_by_type_0 = IncidentCancelledByType0.from_dict(data)

                return cancelled_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IncidentCancelledByType0", None, Unset], data)

        cancelled_by = _parse_cancelled_by(d.pop("cancelled_by", UNSET))

        def _parse_in_triage_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        in_triage_at = _parse_in_triage_at(d.pop("in_triage_at", UNSET))

        def _parse_started_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_detected_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        detected_at = _parse_detected_at(d.pop("detected_at", UNSET))

        def _parse_acknowledged_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_mitigated_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mitigated_at = _parse_mitigated_at(d.pop("mitigated_at", UNSET))

        def _parse_resolved_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        def _parse_closed_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        def _parse_cancelled_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

        incident = cls(
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            sequential_id=sequential_id,
            kind=kind,
            slug=slug,
            parent_incident_id=parent_incident_id,
            duplicate_incident_id=duplicate_incident_id,
            summary=summary,
            private=private,
            source=source,
            status=status,
            url=url,
            short_url=short_url,
            public_title=public_title,
            user=user,
            severity=severity,
            environments=environments,
            incident_types=incident_types,
            services=services,
            functionalities=functionalities,
            groups=groups,
            labels=labels,
            slack_channel_id=slack_channel_id,
            slack_channel_name=slack_channel_name,
            slack_channel_url=slack_channel_url,
            slack_channel_short_url=slack_channel_short_url,
            slack_channel_deep_link=slack_channel_deep_link,
            slack_channel_archived=slack_channel_archived,
            slack_last_message_ts=slack_last_message_ts,
            zoom_meeting_id=zoom_meeting_id,
            zoom_meeting_start_url=zoom_meeting_start_url,
            zoom_meeting_join_url=zoom_meeting_join_url,
            zoom_meeting_password=zoom_meeting_password,
            zoom_meeting_pstn_password=zoom_meeting_pstn_password,
            zoom_meeting_h323_password=zoom_meeting_h323_password,
            zoom_meeting_global_dial_in_numbers=zoom_meeting_global_dial_in_numbers,
            google_drive_id=google_drive_id,
            google_drive_parent_id=google_drive_parent_id,
            google_drive_url=google_drive_url,
            google_meeting_id=google_meeting_id,
            google_meeting_url=google_meeting_url,
            jira_issue_key=jira_issue_key,
            jira_issue_id=jira_issue_id,
            jira_issue_url=jira_issue_url,
            github_issue_id=github_issue_id,
            github_issue_url=github_issue_url,
            gitlab_issue_id=gitlab_issue_id,
            gitlab_issue_url=gitlab_issue_url,
            asana_task_id=asana_task_id,
            asana_task_url=asana_task_url,
            linear_issue_id=linear_issue_id,
            linear_issue_url=linear_issue_url,
            trello_card_id=trello_card_id,
            trello_card_url=trello_card_url,
            zendesk_ticket_id=zendesk_ticket_id,
            zendesk_ticket_url=zendesk_ticket_url,
            pagerduty_incident_id=pagerduty_incident_id,
            pagerduty_incident_number=pagerduty_incident_number,
            pagerduty_incident_url=pagerduty_incident_url,
            opsgenie_incident_id=opsgenie_incident_id,
            opsgenie_incident_url=opsgenie_incident_url,
            opsgenie_alert_id=opsgenie_alert_id,
            opsgenie_alert_url=opsgenie_alert_url,
            service_now_incident_id=service_now_incident_id,
            service_now_incident_key=service_now_incident_key,
            service_now_incident_url=service_now_incident_url,
            mattermost_channel_id=mattermost_channel_id,
            mattermost_channel_name=mattermost_channel_name,
            mattermost_channel_url=mattermost_channel_url,
            confluence_page_id=confluence_page_id,
            confluence_page_url=confluence_page_url,
            datadog_notebook_id=datadog_notebook_id,
            datadog_notebook_url=datadog_notebook_url,
            shortcut_story_id=shortcut_story_id,
            shortcut_story_url=shortcut_story_url,
            shortcut_task_id=shortcut_task_id,
            shortcut_task_url=shortcut_task_url,
            motion_task_id=motion_task_id,
            motion_task_url=motion_task_url,
            clickup_task_id=clickup_task_id,
            clickup_task_url=clickup_task_url,
            victor_ops_incident_id=victor_ops_incident_id,
            victor_ops_incident_url=victor_ops_incident_url,
            quip_page_id=quip_page_id,
            quip_page_url=quip_page_url,
            sharepoint_page_id=sharepoint_page_id,
            sharepoint_page_url=sharepoint_page_url,
            airtable_base_key=airtable_base_key,
            airtable_table_name=airtable_table_name,
            airtable_record_id=airtable_record_id,
            airtable_record_url=airtable_record_url,
            freshservice_ticket_id=freshservice_ticket_id,
            freshservice_ticket_url=freshservice_ticket_url,
            freshservice_task_id=freshservice_task_id,
            freshservice_task_url=freshservice_task_url,
            mitigation_message=mitigation_message,
            resolution_message=resolution_message,
            cancellation_message=cancellation_message,
            scheduled_for=scheduled_for,
            scheduled_until=scheduled_until,
            muted_service_ids=muted_service_ids,
            retrospective_progress_status=retrospective_progress_status,
            in_triage_by=in_triage_by,
            started_by=started_by,
            mitigated_by=mitigated_by,
            resolved_by=resolved_by,
            closed_by=closed_by,
            cancelled_by=cancelled_by,
            in_triage_at=in_triage_at,
            started_at=started_at,
            detected_at=detected_at,
            acknowledged_at=acknowledged_at,
            mitigated_at=mitigated_at,
            resolved_at=resolved_at,
            closed_at=closed_at,
            cancelled_at=cancelled_at,
        )

        incident.additional_properties = d
        return incident

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
