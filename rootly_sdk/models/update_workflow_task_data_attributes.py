from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_action_item_task_params import AddActionItemTaskParams
    from ..models.add_role_task_params import AddRoleTaskParams
    from ..models.add_team_task_params import AddTeamTaskParams
    from ..models.add_to_timeline_task_params import AddToTimelineTaskParams
    from ..models.archive_microsoft_teams_channels_task_params import ArchiveMicrosoftTeamsChannelsTaskParams
    from ..models.archive_slack_channels_task_params import ArchiveSlackChannelsTaskParams
    from ..models.attach_datadog_dashboards_task_params import AttachDatadogDashboardsTaskParams
    from ..models.auto_assign_role_opsgenie_task_params import AutoAssignRoleOpsgenieTaskParams
    from ..models.auto_assign_role_rootly_task_params import AutoAssignRoleRootlyTaskParams
    from ..models.auto_assign_role_victor_ops_task_params import AutoAssignRoleVictorOpsTaskParams
    from ..models.call_people_task_params import CallPeopleTaskParams
    from ..models.change_slack_channel_privacy_task_params import ChangeSlackChannelPrivacyTaskParams
    from ..models.create_airtable_table_record_task_params import CreateAirtableTableRecordTaskParams
    from ..models.create_asana_subtask_task_params import CreateAsanaSubtaskTaskParams
    from ..models.create_asana_task_task_params import CreateAsanaTaskTaskParams
    from ..models.create_clickup_task_task_params import CreateClickupTaskTaskParams
    from ..models.create_confluence_page_task_params import CreateConfluencePageTaskParams
    from ..models.create_datadog_notebook_task_params import CreateDatadogNotebookTaskParams
    from ..models.create_dropbox_paper_page_task_params import CreateDropboxPaperPageTaskParams
    from ..models.create_github_issue_task_params import CreateGithubIssueTaskParams
    from ..models.create_gitlab_issue_task_params import CreateGitlabIssueTaskParams
    from ..models.create_go_to_meeting_task_params import CreateGoToMeetingTaskParams
    from ..models.create_google_calendar_event_task_params import CreateGoogleCalendarEventTaskParams
    from ..models.create_google_docs_page_task_params import CreateGoogleDocsPageTaskParams
    from ..models.create_google_docs_permissions_task_params import CreateGoogleDocsPermissionsTaskParams
    from ..models.create_google_meeting_task_params import CreateGoogleMeetingTaskParams
    from ..models.create_incident_postmortem_task_params import CreateIncidentPostmortemTaskParams
    from ..models.create_incident_task_params import CreateIncidentTaskParams
    from ..models.create_jira_issue_task_params import CreateJiraIssueTaskParams
    from ..models.create_jira_subtask_task_params import CreateJiraSubtaskTaskParams
    from ..models.create_linear_issue_comment_task_params import CreateLinearIssueCommentTaskParams
    from ..models.create_linear_issue_task_params import CreateLinearIssueTaskParams
    from ..models.create_linear_subtask_issue_task_params import CreateLinearSubtaskIssueTaskParams
    from ..models.create_microsoft_teams_channel_task_params import CreateMicrosoftTeamsChannelTaskParams
    from ..models.create_microsoft_teams_meeting_task_params import CreateMicrosoftTeamsMeetingTaskParams
    from ..models.create_motion_task_task_params import CreateMotionTaskTaskParams
    from ..models.create_notion_page_task_params import CreateNotionPageTaskParams
    from ..models.create_opsgenie_alert_task_params import CreateOpsgenieAlertTaskParams
    from ..models.create_outlook_event_task_params import CreateOutlookEventTaskParams
    from ..models.create_pagerduty_status_update_task_params import CreatePagerdutyStatusUpdateTaskParams
    from ..models.create_pagertree_alert_task_params import CreatePagertreeAlertTaskParams
    from ..models.create_quip_page_task_params import CreateQuipPageTaskParams
    from ..models.create_service_now_incident_task_params import CreateServiceNowIncidentTaskParams
    from ..models.create_sharepoint_page_task_params import CreateSharepointPageTaskParams
    from ..models.create_shortcut_task_task_params import CreateShortcutTaskTaskParams
    from ..models.create_slack_channel_task_params import CreateSlackChannelTaskParams
    from ..models.create_trello_card_task_params import CreateTrelloCardTaskParams
    from ..models.create_webex_meeting_task_params import CreateWebexMeetingTaskParams
    from ..models.create_zendesk_jira_link_task_params import CreateZendeskJiraLinkTaskParams
    from ..models.create_zendesk_ticket_task_params import CreateZendeskTicketTaskParams
    from ..models.create_zoom_meeting_task_params import CreateZoomMeetingTaskParams
    from ..models.genius_create_openai_chat_completion_task_params import GeniusCreateOpenaiChatCompletionTaskParams
    from ..models.genius_create_watsonx_chat_completion_task_params import GeniusCreateWatsonxChatCompletionTaskParams
    from ..models.get_alerts_task_params import GetAlertsTaskParams
    from ..models.get_pulses_task_params import GetPulsesTaskParams
    from ..models.http_client_task_params import HttpClientTaskParams
    from ..models.invite_to_microsoft_teams_channel_task_params import InviteToMicrosoftTeamsChannelTaskParams
    from ..models.invite_to_slack_channel_opsgenie_task_params import InviteToSlackChannelOpsgenieTaskParams
    from ..models.invite_to_slack_channel_rootly_task_params import InviteToSlackChannelRootlyTaskParams
    from ..models.invite_to_slack_channel_victor_ops_task_params import InviteToSlackChannelVictorOpsTaskParams
    from ..models.page_opsgenie_on_call_responders_task_params import PageOpsgenieOnCallRespondersTaskParams
    from ..models.page_pagerduty_on_call_responders_task_params import PagePagerdutyOnCallRespondersTaskParams
    from ..models.page_rootly_on_call_responders_task_params import PageRootlyOnCallRespondersTaskParams
    from ..models.print_task_params import PrintTaskParams
    from ..models.publish_incident_task_params import PublishIncidentTaskParams
    from ..models.redis_client_task_params import RedisClientTaskParams
    from ..models.remove_google_docs_permissions_task_params import RemoveGoogleDocsPermissionsTaskParams
    from ..models.rename_microsoft_teams_channel_task_params import RenameMicrosoftTeamsChannelTaskParams
    from ..models.rename_slack_channel_task_params import RenameSlackChannelTaskParams
    from ..models.run_command_heroku_task_params import RunCommandHerokuTaskParams
    from ..models.send_dashboard_report_task_params import SendDashboardReportTaskParams
    from ..models.send_email_task_params import SendEmailTaskParams
    from ..models.send_sms_task_params import SendSmsTaskParams
    from ..models.send_whatsapp_message_task_params import SendWhatsappMessageTaskParams
    from ..models.snapshot_datadog_graph_task_params import SnapshotDatadogGraphTaskParams
    from ..models.snapshot_grafana_dashboard_task_params import SnapshotGrafanaDashboardTaskParams
    from ..models.snapshot_looker_look_task_params import SnapshotLookerLookTaskParams
    from ..models.snapshot_new_relic_graph_task_params import SnapshotNewRelicGraphTaskParams
    from ..models.trigger_workflow_task_params import TriggerWorkflowTaskParams
    from ..models.tweet_twitter_message_task_params import TweetTwitterMessageTaskParams
    from ..models.update_action_item_task_params import UpdateActionItemTaskParams
    from ..models.update_airtable_table_record_task_params import UpdateAirtableTableRecordTaskParams
    from ..models.update_asana_task_task_params import UpdateAsanaTaskTaskParams
    from ..models.update_attached_alerts_task_params import UpdateAttachedAlertsTaskParams
    from ..models.update_clickup_task_task_params import UpdateClickupTaskTaskParams
    from ..models.update_github_issue_task_params import UpdateGithubIssueTaskParams
    from ..models.update_gitlab_issue_task_params import UpdateGitlabIssueTaskParams
    from ..models.update_google_calendar_event_task_params import UpdateGoogleCalendarEventTaskParams
    from ..models.update_google_docs_page_task_params import UpdateGoogleDocsPageTaskParams
    from ..models.update_incident_postmortem_task_params import UpdateIncidentPostmortemTaskParams
    from ..models.update_incident_status_timestamp_task_params import UpdateIncidentStatusTimestampTaskParams
    from ..models.update_incident_task_params import UpdateIncidentTaskParams
    from ..models.update_jira_issue_task_params import UpdateJiraIssueTaskParams
    from ..models.update_linear_issue_task_params import UpdateLinearIssueTaskParams
    from ..models.update_motion_task_task_params import UpdateMotionTaskTaskParams
    from ..models.update_notion_page_task_params import UpdateNotionPageTaskParams
    from ..models.update_opsgenie_alert_task_params import UpdateOpsgenieAlertTaskParams
    from ..models.update_opsgenie_incident_task_params import UpdateOpsgenieIncidentTaskParams
    from ..models.update_pagerduty_incident_task_params import UpdatePagerdutyIncidentTaskParams
    from ..models.update_pagertree_alert_task_params import UpdatePagertreeAlertTaskParams
    from ..models.update_service_now_incident_task_params import UpdateServiceNowIncidentTaskParams
    from ..models.update_shortcut_story_task_params import UpdateShortcutStoryTaskParams
    from ..models.update_shortcut_task_task_params import UpdateShortcutTaskTaskParams
    from ..models.update_slack_channel_topic_task_params import UpdateSlackChannelTopicTaskParams
    from ..models.update_status_task_params import UpdateStatusTaskParams
    from ..models.update_trello_card_task_params import UpdateTrelloCardTaskParams
    from ..models.update_victor_ops_incident_task_params import UpdateVictorOpsIncidentTaskParams
    from ..models.update_zendesk_ticket_task_params import UpdateZendeskTicketTaskParams


T = TypeVar("T", bound="UpdateWorkflowTaskDataAttributes")


@_attrs_define
class UpdateWorkflowTaskDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): Name of the workflow task
        position (Union[Unset, int]): The position of the workflow task
        skip_on_failure (Union[Unset, bool]): Skip workflow task if any failures
        enabled (Union[Unset, bool]): Enable/disable workflow task Default: True.
        task_params (Union['AddActionItemTaskParams', 'AddRoleTaskParams', 'AddTeamTaskParams',
            'AddToTimelineTaskParams', 'ArchiveMicrosoftTeamsChannelsTaskParams', 'ArchiveSlackChannelsTaskParams',
            'AttachDatadogDashboardsTaskParams', 'AutoAssignRoleOpsgenieTaskParams', 'AutoAssignRoleRootlyTaskParams',
            'AutoAssignRoleVictorOpsTaskParams', 'CallPeopleTaskParams', 'ChangeSlackChannelPrivacyTaskParams',
            'CreateAirtableTableRecordTaskParams', 'CreateAsanaSubtaskTaskParams', 'CreateAsanaTaskTaskParams',
            'CreateClickupTaskTaskParams', 'CreateConfluencePageTaskParams', 'CreateDatadogNotebookTaskParams',
            'CreateDropboxPaperPageTaskParams', 'CreateGithubIssueTaskParams', 'CreateGitlabIssueTaskParams',
            'CreateGoToMeetingTaskParams', 'CreateGoogleCalendarEventTaskParams', 'CreateGoogleDocsPageTaskParams',
            'CreateGoogleDocsPermissionsTaskParams', 'CreateGoogleMeetingTaskParams', 'CreateIncidentPostmortemTaskParams',
            'CreateIncidentTaskParams', 'CreateJiraIssueTaskParams', 'CreateJiraSubtaskTaskParams',
            'CreateLinearIssueCommentTaskParams', 'CreateLinearIssueTaskParams', 'CreateLinearSubtaskIssueTaskParams',
            'CreateMicrosoftTeamsChannelTaskParams', 'CreateMicrosoftTeamsMeetingTaskParams', 'CreateMotionTaskTaskParams',
            'CreateNotionPageTaskParams', 'CreateOpsgenieAlertTaskParams', 'CreateOutlookEventTaskParams',
            'CreatePagerdutyStatusUpdateTaskParams', 'CreatePagertreeAlertTaskParams', 'CreateQuipPageTaskParams',
            'CreateServiceNowIncidentTaskParams', 'CreateSharepointPageTaskParams', 'CreateShortcutTaskTaskParams',
            'CreateSlackChannelTaskParams', 'CreateTrelloCardTaskParams', 'CreateWebexMeetingTaskParams',
            'CreateZendeskJiraLinkTaskParams', 'CreateZendeskTicketTaskParams', 'CreateZoomMeetingTaskParams',
            'GeniusCreateOpenaiChatCompletionTaskParams', 'GeniusCreateWatsonxChatCompletionTaskParams',
            'GetAlertsTaskParams', 'GetPulsesTaskParams', 'HttpClientTaskParams', 'InviteToMicrosoftTeamsChannelTaskParams',
            'InviteToSlackChannelOpsgenieTaskParams', 'InviteToSlackChannelRootlyTaskParams',
            'InviteToSlackChannelVictorOpsTaskParams', 'PageOpsgenieOnCallRespondersTaskParams',
            'PagePagerdutyOnCallRespondersTaskParams', 'PageRootlyOnCallRespondersTaskParams', 'PrintTaskParams',
            'PublishIncidentTaskParams', 'RedisClientTaskParams', 'RemoveGoogleDocsPermissionsTaskParams',
            'RenameMicrosoftTeamsChannelTaskParams', 'RenameSlackChannelTaskParams', 'RunCommandHerokuTaskParams',
            'SendDashboardReportTaskParams', 'SendEmailTaskParams', 'SendSmsTaskParams', 'SendWhatsappMessageTaskParams',
            'SnapshotDatadogGraphTaskParams', 'SnapshotGrafanaDashboardTaskParams', 'SnapshotLookerLookTaskParams',
            'SnapshotNewRelicGraphTaskParams', 'TriggerWorkflowTaskParams', 'TweetTwitterMessageTaskParams',
            'UpdateActionItemTaskParams', 'UpdateAirtableTableRecordTaskParams', 'UpdateAsanaTaskTaskParams',
            'UpdateAttachedAlertsTaskParams', 'UpdateClickupTaskTaskParams', 'UpdateGithubIssueTaskParams',
            'UpdateGitlabIssueTaskParams', 'UpdateGoogleCalendarEventTaskParams', 'UpdateGoogleDocsPageTaskParams',
            'UpdateIncidentPostmortemTaskParams', 'UpdateIncidentStatusTimestampTaskParams', 'UpdateIncidentTaskParams',
            'UpdateJiraIssueTaskParams', 'UpdateLinearIssueTaskParams', 'UpdateMotionTaskTaskParams',
            'UpdateNotionPageTaskParams', 'UpdateOpsgenieAlertTaskParams', 'UpdateOpsgenieIncidentTaskParams',
            'UpdatePagerdutyIncidentTaskParams', 'UpdatePagertreeAlertTaskParams', 'UpdateServiceNowIncidentTaskParams',
            'UpdateShortcutStoryTaskParams', 'UpdateShortcutTaskTaskParams', 'UpdateSlackChannelTopicTaskParams',
            'UpdateStatusTaskParams', 'UpdateTrelloCardTaskParams', 'UpdateVictorOpsIncidentTaskParams',
            'UpdateZendeskTicketTaskParams', Any, Unset]):
    """

    name: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    skip_on_failure: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = True
    task_params: Union[
        "AddActionItemTaskParams",
        "AddRoleTaskParams",
        "AddTeamTaskParams",
        "AddToTimelineTaskParams",
        "ArchiveMicrosoftTeamsChannelsTaskParams",
        "ArchiveSlackChannelsTaskParams",
        "AttachDatadogDashboardsTaskParams",
        "AutoAssignRoleOpsgenieTaskParams",
        "AutoAssignRoleRootlyTaskParams",
        "AutoAssignRoleVictorOpsTaskParams",
        "CallPeopleTaskParams",
        "ChangeSlackChannelPrivacyTaskParams",
        "CreateAirtableTableRecordTaskParams",
        "CreateAsanaSubtaskTaskParams",
        "CreateAsanaTaskTaskParams",
        "CreateClickupTaskTaskParams",
        "CreateConfluencePageTaskParams",
        "CreateDatadogNotebookTaskParams",
        "CreateDropboxPaperPageTaskParams",
        "CreateGithubIssueTaskParams",
        "CreateGitlabIssueTaskParams",
        "CreateGoToMeetingTaskParams",
        "CreateGoogleCalendarEventTaskParams",
        "CreateGoogleDocsPageTaskParams",
        "CreateGoogleDocsPermissionsTaskParams",
        "CreateGoogleMeetingTaskParams",
        "CreateIncidentPostmortemTaskParams",
        "CreateIncidentTaskParams",
        "CreateJiraIssueTaskParams",
        "CreateJiraSubtaskTaskParams",
        "CreateLinearIssueCommentTaskParams",
        "CreateLinearIssueTaskParams",
        "CreateLinearSubtaskIssueTaskParams",
        "CreateMicrosoftTeamsChannelTaskParams",
        "CreateMicrosoftTeamsMeetingTaskParams",
        "CreateMotionTaskTaskParams",
        "CreateNotionPageTaskParams",
        "CreateOpsgenieAlertTaskParams",
        "CreateOutlookEventTaskParams",
        "CreatePagerdutyStatusUpdateTaskParams",
        "CreatePagertreeAlertTaskParams",
        "CreateQuipPageTaskParams",
        "CreateServiceNowIncidentTaskParams",
        "CreateSharepointPageTaskParams",
        "CreateShortcutTaskTaskParams",
        "CreateSlackChannelTaskParams",
        "CreateTrelloCardTaskParams",
        "CreateWebexMeetingTaskParams",
        "CreateZendeskJiraLinkTaskParams",
        "CreateZendeskTicketTaskParams",
        "CreateZoomMeetingTaskParams",
        "GeniusCreateOpenaiChatCompletionTaskParams",
        "GeniusCreateWatsonxChatCompletionTaskParams",
        "GetAlertsTaskParams",
        "GetPulsesTaskParams",
        "HttpClientTaskParams",
        "InviteToMicrosoftTeamsChannelTaskParams",
        "InviteToSlackChannelOpsgenieTaskParams",
        "InviteToSlackChannelRootlyTaskParams",
        "InviteToSlackChannelVictorOpsTaskParams",
        "PageOpsgenieOnCallRespondersTaskParams",
        "PagePagerdutyOnCallRespondersTaskParams",
        "PageRootlyOnCallRespondersTaskParams",
        "PrintTaskParams",
        "PublishIncidentTaskParams",
        "RedisClientTaskParams",
        "RemoveGoogleDocsPermissionsTaskParams",
        "RenameMicrosoftTeamsChannelTaskParams",
        "RenameSlackChannelTaskParams",
        "RunCommandHerokuTaskParams",
        "SendDashboardReportTaskParams",
        "SendEmailTaskParams",
        "SendSmsTaskParams",
        "SendWhatsappMessageTaskParams",
        "SnapshotDatadogGraphTaskParams",
        "SnapshotGrafanaDashboardTaskParams",
        "SnapshotLookerLookTaskParams",
        "SnapshotNewRelicGraphTaskParams",
        "TriggerWorkflowTaskParams",
        "TweetTwitterMessageTaskParams",
        "UpdateActionItemTaskParams",
        "UpdateAirtableTableRecordTaskParams",
        "UpdateAsanaTaskTaskParams",
        "UpdateAttachedAlertsTaskParams",
        "UpdateClickupTaskTaskParams",
        "UpdateGithubIssueTaskParams",
        "UpdateGitlabIssueTaskParams",
        "UpdateGoogleCalendarEventTaskParams",
        "UpdateGoogleDocsPageTaskParams",
        "UpdateIncidentPostmortemTaskParams",
        "UpdateIncidentStatusTimestampTaskParams",
        "UpdateIncidentTaskParams",
        "UpdateJiraIssueTaskParams",
        "UpdateLinearIssueTaskParams",
        "UpdateMotionTaskTaskParams",
        "UpdateNotionPageTaskParams",
        "UpdateOpsgenieAlertTaskParams",
        "UpdateOpsgenieIncidentTaskParams",
        "UpdatePagerdutyIncidentTaskParams",
        "UpdatePagertreeAlertTaskParams",
        "UpdateServiceNowIncidentTaskParams",
        "UpdateShortcutStoryTaskParams",
        "UpdateShortcutTaskTaskParams",
        "UpdateSlackChannelTopicTaskParams",
        "UpdateStatusTaskParams",
        "UpdateTrelloCardTaskParams",
        "UpdateVictorOpsIncidentTaskParams",
        "UpdateZendeskTicketTaskParams",
        Any,
        Unset,
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_action_item_task_params import AddActionItemTaskParams
        from ..models.add_role_task_params import AddRoleTaskParams
        from ..models.add_team_task_params import AddTeamTaskParams
        from ..models.add_to_timeline_task_params import AddToTimelineTaskParams
        from ..models.archive_microsoft_teams_channels_task_params import ArchiveMicrosoftTeamsChannelsTaskParams
        from ..models.archive_slack_channels_task_params import ArchiveSlackChannelsTaskParams
        from ..models.attach_datadog_dashboards_task_params import AttachDatadogDashboardsTaskParams
        from ..models.auto_assign_role_opsgenie_task_params import AutoAssignRoleOpsgenieTaskParams
        from ..models.auto_assign_role_rootly_task_params import AutoAssignRoleRootlyTaskParams
        from ..models.auto_assign_role_victor_ops_task_params import AutoAssignRoleVictorOpsTaskParams
        from ..models.call_people_task_params import CallPeopleTaskParams
        from ..models.change_slack_channel_privacy_task_params import ChangeSlackChannelPrivacyTaskParams
        from ..models.create_airtable_table_record_task_params import CreateAirtableTableRecordTaskParams
        from ..models.create_asana_subtask_task_params import CreateAsanaSubtaskTaskParams
        from ..models.create_asana_task_task_params import CreateAsanaTaskTaskParams
        from ..models.create_clickup_task_task_params import CreateClickupTaskTaskParams
        from ..models.create_confluence_page_task_params import CreateConfluencePageTaskParams
        from ..models.create_datadog_notebook_task_params import CreateDatadogNotebookTaskParams
        from ..models.create_dropbox_paper_page_task_params import CreateDropboxPaperPageTaskParams
        from ..models.create_github_issue_task_params import CreateGithubIssueTaskParams
        from ..models.create_gitlab_issue_task_params import CreateGitlabIssueTaskParams
        from ..models.create_go_to_meeting_task_params import CreateGoToMeetingTaskParams
        from ..models.create_google_calendar_event_task_params import CreateGoogleCalendarEventTaskParams
        from ..models.create_google_docs_page_task_params import CreateGoogleDocsPageTaskParams
        from ..models.create_google_docs_permissions_task_params import CreateGoogleDocsPermissionsTaskParams
        from ..models.create_google_meeting_task_params import CreateGoogleMeetingTaskParams
        from ..models.create_incident_postmortem_task_params import CreateIncidentPostmortemTaskParams
        from ..models.create_incident_task_params import CreateIncidentTaskParams
        from ..models.create_jira_issue_task_params import CreateJiraIssueTaskParams
        from ..models.create_jira_subtask_task_params import CreateJiraSubtaskTaskParams
        from ..models.create_linear_issue_comment_task_params import CreateLinearIssueCommentTaskParams
        from ..models.create_linear_issue_task_params import CreateLinearIssueTaskParams
        from ..models.create_linear_subtask_issue_task_params import CreateLinearSubtaskIssueTaskParams
        from ..models.create_microsoft_teams_channel_task_params import CreateMicrosoftTeamsChannelTaskParams
        from ..models.create_microsoft_teams_meeting_task_params import CreateMicrosoftTeamsMeetingTaskParams
        from ..models.create_motion_task_task_params import CreateMotionTaskTaskParams
        from ..models.create_notion_page_task_params import CreateNotionPageTaskParams
        from ..models.create_opsgenie_alert_task_params import CreateOpsgenieAlertTaskParams
        from ..models.create_outlook_event_task_params import CreateOutlookEventTaskParams
        from ..models.create_pagerduty_status_update_task_params import CreatePagerdutyStatusUpdateTaskParams
        from ..models.create_pagertree_alert_task_params import CreatePagertreeAlertTaskParams
        from ..models.create_quip_page_task_params import CreateQuipPageTaskParams
        from ..models.create_service_now_incident_task_params import CreateServiceNowIncidentTaskParams
        from ..models.create_sharepoint_page_task_params import CreateSharepointPageTaskParams
        from ..models.create_shortcut_task_task_params import CreateShortcutTaskTaskParams
        from ..models.create_slack_channel_task_params import CreateSlackChannelTaskParams
        from ..models.create_trello_card_task_params import CreateTrelloCardTaskParams
        from ..models.create_webex_meeting_task_params import CreateWebexMeetingTaskParams
        from ..models.create_zendesk_jira_link_task_params import CreateZendeskJiraLinkTaskParams
        from ..models.create_zendesk_ticket_task_params import CreateZendeskTicketTaskParams
        from ..models.create_zoom_meeting_task_params import CreateZoomMeetingTaskParams
        from ..models.genius_create_openai_chat_completion_task_params import GeniusCreateOpenaiChatCompletionTaskParams
        from ..models.genius_create_watsonx_chat_completion_task_params import (
            GeniusCreateWatsonxChatCompletionTaskParams,
        )
        from ..models.get_alerts_task_params import GetAlertsTaskParams
        from ..models.get_pulses_task_params import GetPulsesTaskParams
        from ..models.http_client_task_params import HttpClientTaskParams
        from ..models.invite_to_microsoft_teams_channel_task_params import InviteToMicrosoftTeamsChannelTaskParams
        from ..models.invite_to_slack_channel_opsgenie_task_params import InviteToSlackChannelOpsgenieTaskParams
        from ..models.invite_to_slack_channel_rootly_task_params import InviteToSlackChannelRootlyTaskParams
        from ..models.invite_to_slack_channel_victor_ops_task_params import InviteToSlackChannelVictorOpsTaskParams
        from ..models.page_opsgenie_on_call_responders_task_params import PageOpsgenieOnCallRespondersTaskParams
        from ..models.page_pagerduty_on_call_responders_task_params import PagePagerdutyOnCallRespondersTaskParams
        from ..models.page_rootly_on_call_responders_task_params import PageRootlyOnCallRespondersTaskParams
        from ..models.print_task_params import PrintTaskParams
        from ..models.publish_incident_task_params import PublishIncidentTaskParams
        from ..models.redis_client_task_params import RedisClientTaskParams
        from ..models.remove_google_docs_permissions_task_params import RemoveGoogleDocsPermissionsTaskParams
        from ..models.rename_microsoft_teams_channel_task_params import RenameMicrosoftTeamsChannelTaskParams
        from ..models.rename_slack_channel_task_params import RenameSlackChannelTaskParams
        from ..models.run_command_heroku_task_params import RunCommandHerokuTaskParams
        from ..models.send_dashboard_report_task_params import SendDashboardReportTaskParams
        from ..models.send_email_task_params import SendEmailTaskParams
        from ..models.send_sms_task_params import SendSmsTaskParams
        from ..models.send_whatsapp_message_task_params import SendWhatsappMessageTaskParams
        from ..models.snapshot_datadog_graph_task_params import SnapshotDatadogGraphTaskParams
        from ..models.snapshot_grafana_dashboard_task_params import SnapshotGrafanaDashboardTaskParams
        from ..models.snapshot_looker_look_task_params import SnapshotLookerLookTaskParams
        from ..models.snapshot_new_relic_graph_task_params import SnapshotNewRelicGraphTaskParams
        from ..models.trigger_workflow_task_params import TriggerWorkflowTaskParams
        from ..models.tweet_twitter_message_task_params import TweetTwitterMessageTaskParams
        from ..models.update_action_item_task_params import UpdateActionItemTaskParams
        from ..models.update_airtable_table_record_task_params import UpdateAirtableTableRecordTaskParams
        from ..models.update_asana_task_task_params import UpdateAsanaTaskTaskParams
        from ..models.update_attached_alerts_task_params import UpdateAttachedAlertsTaskParams
        from ..models.update_clickup_task_task_params import UpdateClickupTaskTaskParams
        from ..models.update_github_issue_task_params import UpdateGithubIssueTaskParams
        from ..models.update_gitlab_issue_task_params import UpdateGitlabIssueTaskParams
        from ..models.update_google_calendar_event_task_params import UpdateGoogleCalendarEventTaskParams
        from ..models.update_google_docs_page_task_params import UpdateGoogleDocsPageTaskParams
        from ..models.update_incident_postmortem_task_params import UpdateIncidentPostmortemTaskParams
        from ..models.update_incident_status_timestamp_task_params import UpdateIncidentStatusTimestampTaskParams
        from ..models.update_incident_task_params import UpdateIncidentTaskParams
        from ..models.update_jira_issue_task_params import UpdateJiraIssueTaskParams
        from ..models.update_linear_issue_task_params import UpdateLinearIssueTaskParams
        from ..models.update_motion_task_task_params import UpdateMotionTaskTaskParams
        from ..models.update_notion_page_task_params import UpdateNotionPageTaskParams
        from ..models.update_opsgenie_alert_task_params import UpdateOpsgenieAlertTaskParams
        from ..models.update_opsgenie_incident_task_params import UpdateOpsgenieIncidentTaskParams
        from ..models.update_pagerduty_incident_task_params import UpdatePagerdutyIncidentTaskParams
        from ..models.update_pagertree_alert_task_params import UpdatePagertreeAlertTaskParams
        from ..models.update_service_now_incident_task_params import UpdateServiceNowIncidentTaskParams
        from ..models.update_shortcut_story_task_params import UpdateShortcutStoryTaskParams
        from ..models.update_shortcut_task_task_params import UpdateShortcutTaskTaskParams
        from ..models.update_slack_channel_topic_task_params import UpdateSlackChannelTopicTaskParams
        from ..models.update_status_task_params import UpdateStatusTaskParams
        from ..models.update_trello_card_task_params import UpdateTrelloCardTaskParams
        from ..models.update_victor_ops_incident_task_params import UpdateVictorOpsIncidentTaskParams
        from ..models.update_zendesk_ticket_task_params import UpdateZendeskTicketTaskParams

        name = self.name

        position = self.position

        skip_on_failure = self.skip_on_failure

        enabled = self.enabled

        task_params: Union[Any, Unset, dict[str, Any]]
        if isinstance(self.task_params, Unset):
            task_params = UNSET
        elif isinstance(self.task_params, AddActionItemTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateActionItemTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddRoleTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddTeamTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddToTimelineTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, ArchiveSlackChannelsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AttachDatadogDashboardsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRoleOpsgenieTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRoleRootlyTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdatePagerdutyIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreatePagerdutyStatusUpdateTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreatePagertreeAlertTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdatePagertreeAlertTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRoleVictorOpsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CallPeopleTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateAirtableTableRecordTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateAsanaSubtaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateAsanaTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateConfluencePageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateDatadogNotebookTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateDropboxPaperPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGithubIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGitlabIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateOutlookEventTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGoogleCalendarEventTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateGoogleDocsPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateGoogleCalendarEventTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateSharepointPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGoogleDocsPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGoogleDocsPermissionsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, RemoveGoogleDocsPermissionsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateQuipPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGoogleMeetingTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGoToMeetingTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateIncidentPostmortemTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateJiraIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateJiraSubtaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateLinearIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateLinearSubtaskIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateLinearIssueCommentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateMicrosoftTeamsMeetingTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateMicrosoftTeamsChannelTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, ArchiveMicrosoftTeamsChannelsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, RenameMicrosoftTeamsChannelTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToMicrosoftTeamsChannelTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateNotionPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateNotionPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateServiceNowIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateShortcutTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateTrelloCardTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateWebexMeetingTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateZendeskTicketTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateZendeskJiraLinkTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateClickupTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateMotionTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateZoomMeetingTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, GetPulsesTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, GetAlertsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, HttpClientTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelOpsgenieTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelRootlyTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelVictorOpsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PageOpsgenieOnCallRespondersTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateOpsgenieAlertTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateOpsgenieAlertTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateOpsgenieIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PageRootlyOnCallRespondersTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PagePagerdutyOnCallRespondersTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateVictorOpsIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PrintTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PublishIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, RedisClientTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, RenameSlackChannelTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, ChangeSlackChannelPrivacyTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, RunCommandHerokuTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendEmailTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendDashboardReportTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateSlackChannelTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendSmsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendWhatsappMessageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SnapshotDatadogGraphTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SnapshotGrafanaDashboardTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SnapshotLookerLookTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SnapshotNewRelicGraphTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, TweetTwitterMessageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateAirtableTableRecordTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateAsanaTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateGithubIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateGitlabIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateIncidentPostmortemTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateJiraIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateLinearIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateServiceNowIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateShortcutStoryTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateShortcutTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateSlackChannelTopicTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateStatusTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateIncidentStatusTimestampTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateTrelloCardTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateClickupTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateMotionTaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateZendeskTicketTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateAttachedAlertsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, TriggerWorkflowTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, GeniusCreateOpenaiChatCompletionTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, GeniusCreateWatsonxChatCompletionTaskParams):
            task_params = self.task_params.to_dict()
        else:
            task_params = self.task_params

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if skip_on_failure is not UNSET:
            field_dict["skip_on_failure"] = skip_on_failure
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if task_params is not UNSET:
            field_dict["task_params"] = task_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.add_action_item_task_params import AddActionItemTaskParams
        from ..models.add_role_task_params import AddRoleTaskParams
        from ..models.add_team_task_params import AddTeamTaskParams
        from ..models.add_to_timeline_task_params import AddToTimelineTaskParams
        from ..models.archive_microsoft_teams_channels_task_params import ArchiveMicrosoftTeamsChannelsTaskParams
        from ..models.archive_slack_channels_task_params import ArchiveSlackChannelsTaskParams
        from ..models.attach_datadog_dashboards_task_params import AttachDatadogDashboardsTaskParams
        from ..models.auto_assign_role_opsgenie_task_params import AutoAssignRoleOpsgenieTaskParams
        from ..models.auto_assign_role_rootly_task_params import AutoAssignRoleRootlyTaskParams
        from ..models.auto_assign_role_victor_ops_task_params import AutoAssignRoleVictorOpsTaskParams
        from ..models.call_people_task_params import CallPeopleTaskParams
        from ..models.change_slack_channel_privacy_task_params import ChangeSlackChannelPrivacyTaskParams
        from ..models.create_airtable_table_record_task_params import CreateAirtableTableRecordTaskParams
        from ..models.create_asana_subtask_task_params import CreateAsanaSubtaskTaskParams
        from ..models.create_asana_task_task_params import CreateAsanaTaskTaskParams
        from ..models.create_clickup_task_task_params import CreateClickupTaskTaskParams
        from ..models.create_confluence_page_task_params import CreateConfluencePageTaskParams
        from ..models.create_datadog_notebook_task_params import CreateDatadogNotebookTaskParams
        from ..models.create_dropbox_paper_page_task_params import CreateDropboxPaperPageTaskParams
        from ..models.create_github_issue_task_params import CreateGithubIssueTaskParams
        from ..models.create_gitlab_issue_task_params import CreateGitlabIssueTaskParams
        from ..models.create_go_to_meeting_task_params import CreateGoToMeetingTaskParams
        from ..models.create_google_calendar_event_task_params import CreateGoogleCalendarEventTaskParams
        from ..models.create_google_docs_page_task_params import CreateGoogleDocsPageTaskParams
        from ..models.create_google_docs_permissions_task_params import CreateGoogleDocsPermissionsTaskParams
        from ..models.create_google_meeting_task_params import CreateGoogleMeetingTaskParams
        from ..models.create_incident_postmortem_task_params import CreateIncidentPostmortemTaskParams
        from ..models.create_incident_task_params import CreateIncidentTaskParams
        from ..models.create_jira_issue_task_params import CreateJiraIssueTaskParams
        from ..models.create_jira_subtask_task_params import CreateJiraSubtaskTaskParams
        from ..models.create_linear_issue_comment_task_params import CreateLinearIssueCommentTaskParams
        from ..models.create_linear_issue_task_params import CreateLinearIssueTaskParams
        from ..models.create_linear_subtask_issue_task_params import CreateLinearSubtaskIssueTaskParams
        from ..models.create_microsoft_teams_channel_task_params import CreateMicrosoftTeamsChannelTaskParams
        from ..models.create_microsoft_teams_meeting_task_params import CreateMicrosoftTeamsMeetingTaskParams
        from ..models.create_motion_task_task_params import CreateMotionTaskTaskParams
        from ..models.create_notion_page_task_params import CreateNotionPageTaskParams
        from ..models.create_opsgenie_alert_task_params import CreateOpsgenieAlertTaskParams
        from ..models.create_outlook_event_task_params import CreateOutlookEventTaskParams
        from ..models.create_pagerduty_status_update_task_params import CreatePagerdutyStatusUpdateTaskParams
        from ..models.create_pagertree_alert_task_params import CreatePagertreeAlertTaskParams
        from ..models.create_quip_page_task_params import CreateQuipPageTaskParams
        from ..models.create_service_now_incident_task_params import CreateServiceNowIncidentTaskParams
        from ..models.create_sharepoint_page_task_params import CreateSharepointPageTaskParams
        from ..models.create_shortcut_task_task_params import CreateShortcutTaskTaskParams
        from ..models.create_slack_channel_task_params import CreateSlackChannelTaskParams
        from ..models.create_trello_card_task_params import CreateTrelloCardTaskParams
        from ..models.create_webex_meeting_task_params import CreateWebexMeetingTaskParams
        from ..models.create_zendesk_jira_link_task_params import CreateZendeskJiraLinkTaskParams
        from ..models.create_zendesk_ticket_task_params import CreateZendeskTicketTaskParams
        from ..models.create_zoom_meeting_task_params import CreateZoomMeetingTaskParams
        from ..models.genius_create_openai_chat_completion_task_params import GeniusCreateOpenaiChatCompletionTaskParams
        from ..models.genius_create_watsonx_chat_completion_task_params import (
            GeniusCreateWatsonxChatCompletionTaskParams,
        )
        from ..models.get_alerts_task_params import GetAlertsTaskParams
        from ..models.get_pulses_task_params import GetPulsesTaskParams
        from ..models.http_client_task_params import HttpClientTaskParams
        from ..models.invite_to_microsoft_teams_channel_task_params import InviteToMicrosoftTeamsChannelTaskParams
        from ..models.invite_to_slack_channel_opsgenie_task_params import InviteToSlackChannelOpsgenieTaskParams
        from ..models.invite_to_slack_channel_rootly_task_params import InviteToSlackChannelRootlyTaskParams
        from ..models.invite_to_slack_channel_victor_ops_task_params import InviteToSlackChannelVictorOpsTaskParams
        from ..models.page_opsgenie_on_call_responders_task_params import PageOpsgenieOnCallRespondersTaskParams
        from ..models.page_pagerduty_on_call_responders_task_params import PagePagerdutyOnCallRespondersTaskParams
        from ..models.page_rootly_on_call_responders_task_params import PageRootlyOnCallRespondersTaskParams
        from ..models.print_task_params import PrintTaskParams
        from ..models.publish_incident_task_params import PublishIncidentTaskParams
        from ..models.redis_client_task_params import RedisClientTaskParams
        from ..models.remove_google_docs_permissions_task_params import RemoveGoogleDocsPermissionsTaskParams
        from ..models.rename_microsoft_teams_channel_task_params import RenameMicrosoftTeamsChannelTaskParams
        from ..models.rename_slack_channel_task_params import RenameSlackChannelTaskParams
        from ..models.run_command_heroku_task_params import RunCommandHerokuTaskParams
        from ..models.send_dashboard_report_task_params import SendDashboardReportTaskParams
        from ..models.send_email_task_params import SendEmailTaskParams
        from ..models.send_sms_task_params import SendSmsTaskParams
        from ..models.send_whatsapp_message_task_params import SendWhatsappMessageTaskParams
        from ..models.snapshot_datadog_graph_task_params import SnapshotDatadogGraphTaskParams
        from ..models.snapshot_grafana_dashboard_task_params import SnapshotGrafanaDashboardTaskParams
        from ..models.snapshot_looker_look_task_params import SnapshotLookerLookTaskParams
        from ..models.snapshot_new_relic_graph_task_params import SnapshotNewRelicGraphTaskParams
        from ..models.trigger_workflow_task_params import TriggerWorkflowTaskParams
        from ..models.tweet_twitter_message_task_params import TweetTwitterMessageTaskParams
        from ..models.update_action_item_task_params import UpdateActionItemTaskParams
        from ..models.update_airtable_table_record_task_params import UpdateAirtableTableRecordTaskParams
        from ..models.update_asana_task_task_params import UpdateAsanaTaskTaskParams
        from ..models.update_attached_alerts_task_params import UpdateAttachedAlertsTaskParams
        from ..models.update_clickup_task_task_params import UpdateClickupTaskTaskParams
        from ..models.update_github_issue_task_params import UpdateGithubIssueTaskParams
        from ..models.update_gitlab_issue_task_params import UpdateGitlabIssueTaskParams
        from ..models.update_google_calendar_event_task_params import UpdateGoogleCalendarEventTaskParams
        from ..models.update_google_docs_page_task_params import UpdateGoogleDocsPageTaskParams
        from ..models.update_incident_postmortem_task_params import UpdateIncidentPostmortemTaskParams
        from ..models.update_incident_status_timestamp_task_params import UpdateIncidentStatusTimestampTaskParams
        from ..models.update_incident_task_params import UpdateIncidentTaskParams
        from ..models.update_jira_issue_task_params import UpdateJiraIssueTaskParams
        from ..models.update_linear_issue_task_params import UpdateLinearIssueTaskParams
        from ..models.update_motion_task_task_params import UpdateMotionTaskTaskParams
        from ..models.update_notion_page_task_params import UpdateNotionPageTaskParams
        from ..models.update_opsgenie_alert_task_params import UpdateOpsgenieAlertTaskParams
        from ..models.update_opsgenie_incident_task_params import UpdateOpsgenieIncidentTaskParams
        from ..models.update_pagerduty_incident_task_params import UpdatePagerdutyIncidentTaskParams
        from ..models.update_pagertree_alert_task_params import UpdatePagertreeAlertTaskParams
        from ..models.update_service_now_incident_task_params import UpdateServiceNowIncidentTaskParams
        from ..models.update_shortcut_story_task_params import UpdateShortcutStoryTaskParams
        from ..models.update_shortcut_task_task_params import UpdateShortcutTaskTaskParams
        from ..models.update_slack_channel_topic_task_params import UpdateSlackChannelTopicTaskParams
        from ..models.update_status_task_params import UpdateStatusTaskParams
        from ..models.update_trello_card_task_params import UpdateTrelloCardTaskParams
        from ..models.update_victor_ops_incident_task_params import UpdateVictorOpsIncidentTaskParams
        from ..models.update_zendesk_ticket_task_params import UpdateZendeskTicketTaskParams

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        position = d.pop("position", UNSET)

        skip_on_failure = d.pop("skip_on_failure", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_task_params(
            data: object,
        ) -> Union[
            "AddActionItemTaskParams",
            "AddRoleTaskParams",
            "AddTeamTaskParams",
            "AddToTimelineTaskParams",
            "ArchiveMicrosoftTeamsChannelsTaskParams",
            "ArchiveSlackChannelsTaskParams",
            "AttachDatadogDashboardsTaskParams",
            "AutoAssignRoleOpsgenieTaskParams",
            "AutoAssignRoleRootlyTaskParams",
            "AutoAssignRoleVictorOpsTaskParams",
            "CallPeopleTaskParams",
            "ChangeSlackChannelPrivacyTaskParams",
            "CreateAirtableTableRecordTaskParams",
            "CreateAsanaSubtaskTaskParams",
            "CreateAsanaTaskTaskParams",
            "CreateClickupTaskTaskParams",
            "CreateConfluencePageTaskParams",
            "CreateDatadogNotebookTaskParams",
            "CreateDropboxPaperPageTaskParams",
            "CreateGithubIssueTaskParams",
            "CreateGitlabIssueTaskParams",
            "CreateGoToMeetingTaskParams",
            "CreateGoogleCalendarEventTaskParams",
            "CreateGoogleDocsPageTaskParams",
            "CreateGoogleDocsPermissionsTaskParams",
            "CreateGoogleMeetingTaskParams",
            "CreateIncidentPostmortemTaskParams",
            "CreateIncidentTaskParams",
            "CreateJiraIssueTaskParams",
            "CreateJiraSubtaskTaskParams",
            "CreateLinearIssueCommentTaskParams",
            "CreateLinearIssueTaskParams",
            "CreateLinearSubtaskIssueTaskParams",
            "CreateMicrosoftTeamsChannelTaskParams",
            "CreateMicrosoftTeamsMeetingTaskParams",
            "CreateMotionTaskTaskParams",
            "CreateNotionPageTaskParams",
            "CreateOpsgenieAlertTaskParams",
            "CreateOutlookEventTaskParams",
            "CreatePagerdutyStatusUpdateTaskParams",
            "CreatePagertreeAlertTaskParams",
            "CreateQuipPageTaskParams",
            "CreateServiceNowIncidentTaskParams",
            "CreateSharepointPageTaskParams",
            "CreateShortcutTaskTaskParams",
            "CreateSlackChannelTaskParams",
            "CreateTrelloCardTaskParams",
            "CreateWebexMeetingTaskParams",
            "CreateZendeskJiraLinkTaskParams",
            "CreateZendeskTicketTaskParams",
            "CreateZoomMeetingTaskParams",
            "GeniusCreateOpenaiChatCompletionTaskParams",
            "GeniusCreateWatsonxChatCompletionTaskParams",
            "GetAlertsTaskParams",
            "GetPulsesTaskParams",
            "HttpClientTaskParams",
            "InviteToMicrosoftTeamsChannelTaskParams",
            "InviteToSlackChannelOpsgenieTaskParams",
            "InviteToSlackChannelRootlyTaskParams",
            "InviteToSlackChannelVictorOpsTaskParams",
            "PageOpsgenieOnCallRespondersTaskParams",
            "PagePagerdutyOnCallRespondersTaskParams",
            "PageRootlyOnCallRespondersTaskParams",
            "PrintTaskParams",
            "PublishIncidentTaskParams",
            "RedisClientTaskParams",
            "RemoveGoogleDocsPermissionsTaskParams",
            "RenameMicrosoftTeamsChannelTaskParams",
            "RenameSlackChannelTaskParams",
            "RunCommandHerokuTaskParams",
            "SendDashboardReportTaskParams",
            "SendEmailTaskParams",
            "SendSmsTaskParams",
            "SendWhatsappMessageTaskParams",
            "SnapshotDatadogGraphTaskParams",
            "SnapshotGrafanaDashboardTaskParams",
            "SnapshotLookerLookTaskParams",
            "SnapshotNewRelicGraphTaskParams",
            "TriggerWorkflowTaskParams",
            "TweetTwitterMessageTaskParams",
            "UpdateActionItemTaskParams",
            "UpdateAirtableTableRecordTaskParams",
            "UpdateAsanaTaskTaskParams",
            "UpdateAttachedAlertsTaskParams",
            "UpdateClickupTaskTaskParams",
            "UpdateGithubIssueTaskParams",
            "UpdateGitlabIssueTaskParams",
            "UpdateGoogleCalendarEventTaskParams",
            "UpdateGoogleDocsPageTaskParams",
            "UpdateIncidentPostmortemTaskParams",
            "UpdateIncidentStatusTimestampTaskParams",
            "UpdateIncidentTaskParams",
            "UpdateJiraIssueTaskParams",
            "UpdateLinearIssueTaskParams",
            "UpdateMotionTaskTaskParams",
            "UpdateNotionPageTaskParams",
            "UpdateOpsgenieAlertTaskParams",
            "UpdateOpsgenieIncidentTaskParams",
            "UpdatePagerdutyIncidentTaskParams",
            "UpdatePagertreeAlertTaskParams",
            "UpdateServiceNowIncidentTaskParams",
            "UpdateShortcutStoryTaskParams",
            "UpdateShortcutTaskTaskParams",
            "UpdateSlackChannelTopicTaskParams",
            "UpdateStatusTaskParams",
            "UpdateTrelloCardTaskParams",
            "UpdateVictorOpsIncidentTaskParams",
            "UpdateZendeskTicketTaskParams",
            Any,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_0 = AddActionItemTaskParams.from_dict(data)

                return task_params_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_1 = UpdateActionItemTaskParams.from_dict(data)

                return task_params_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_2 = AddRoleTaskParams.from_dict(data)

                return task_params_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_4 = AddTeamTaskParams.from_dict(data)

                return task_params_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_5 = AddToTimelineTaskParams.from_dict(data)

                return task_params_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_6 = ArchiveSlackChannelsTaskParams.from_dict(data)

                return task_params_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_7 = AttachDatadogDashboardsTaskParams.from_dict(data)

                return task_params_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_8 = AutoAssignRoleOpsgenieTaskParams.from_dict(data)

                return task_params_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_9 = AutoAssignRoleRootlyTaskParams.from_dict(data)

                return task_params_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_11 = UpdatePagerdutyIncidentTaskParams.from_dict(data)

                return task_params_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_12 = CreatePagerdutyStatusUpdateTaskParams.from_dict(data)

                return task_params_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_13 = CreatePagertreeAlertTaskParams.from_dict(data)

                return task_params_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_14 = UpdatePagertreeAlertTaskParams.from_dict(data)

                return task_params_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_15 = AutoAssignRoleVictorOpsTaskParams.from_dict(data)

                return task_params_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_16 = CallPeopleTaskParams.from_dict(data)

                return task_params_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_17 = CreateAirtableTableRecordTaskParams.from_dict(data)

                return task_params_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_18 = CreateAsanaSubtaskTaskParams.from_dict(data)

                return task_params_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_19 = CreateAsanaTaskTaskParams.from_dict(data)

                return task_params_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_20 = CreateConfluencePageTaskParams.from_dict(data)

                return task_params_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_21 = CreateDatadogNotebookTaskParams.from_dict(data)

                return task_params_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_22 = CreateDropboxPaperPageTaskParams.from_dict(data)

                return task_params_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_23 = CreateGithubIssueTaskParams.from_dict(data)

                return task_params_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_24 = CreateGitlabIssueTaskParams.from_dict(data)

                return task_params_type_24
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_25 = CreateOutlookEventTaskParams.from_dict(data)

                return task_params_type_25
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_26 = CreateGoogleCalendarEventTaskParams.from_dict(data)

                return task_params_type_26
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_27 = UpdateGoogleDocsPageTaskParams.from_dict(data)

                return task_params_type_27
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_28 = UpdateGoogleCalendarEventTaskParams.from_dict(data)

                return task_params_type_28
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_29 = CreateSharepointPageTaskParams.from_dict(data)

                return task_params_type_29
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_30 = CreateGoogleDocsPageTaskParams.from_dict(data)

                return task_params_type_30
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_31 = CreateGoogleDocsPermissionsTaskParams.from_dict(data)

                return task_params_type_31
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_32 = RemoveGoogleDocsPermissionsTaskParams.from_dict(data)

                return task_params_type_32
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_33 = CreateQuipPageTaskParams.from_dict(data)

                return task_params_type_33
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_34 = CreateGoogleMeetingTaskParams.from_dict(data)

                return task_params_type_34
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_35 = CreateGoToMeetingTaskParams.from_dict(data)

                return task_params_type_35
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_36 = CreateIncidentTaskParams.from_dict(data)

                return task_params_type_36
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_37 = CreateIncidentPostmortemTaskParams.from_dict(data)

                return task_params_type_37
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_38 = CreateJiraIssueTaskParams.from_dict(data)

                return task_params_type_38
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_39 = CreateJiraSubtaskTaskParams.from_dict(data)

                return task_params_type_39
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_40 = CreateLinearIssueTaskParams.from_dict(data)

                return task_params_type_40
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_41 = CreateLinearSubtaskIssueTaskParams.from_dict(data)

                return task_params_type_41
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_42 = CreateLinearIssueCommentTaskParams.from_dict(data)

                return task_params_type_42
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_43 = CreateMicrosoftTeamsMeetingTaskParams.from_dict(data)

                return task_params_type_43
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_44 = CreateMicrosoftTeamsChannelTaskParams.from_dict(data)

                return task_params_type_44
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_46 = ArchiveMicrosoftTeamsChannelsTaskParams.from_dict(data)

                return task_params_type_46
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_47 = RenameMicrosoftTeamsChannelTaskParams.from_dict(data)

                return task_params_type_47
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_48 = InviteToMicrosoftTeamsChannelTaskParams.from_dict(data)

                return task_params_type_48
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_49 = CreateNotionPageTaskParams.from_dict(data)

                return task_params_type_49
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_52 = UpdateNotionPageTaskParams.from_dict(data)

                return task_params_type_52
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_53 = CreateServiceNowIncidentTaskParams.from_dict(data)

                return task_params_type_53
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_55 = CreateShortcutTaskTaskParams.from_dict(data)

                return task_params_type_55
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_56 = CreateTrelloCardTaskParams.from_dict(data)

                return task_params_type_56
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_57 = CreateWebexMeetingTaskParams.from_dict(data)

                return task_params_type_57
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_58 = CreateZendeskTicketTaskParams.from_dict(data)

                return task_params_type_58
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_59 = CreateZendeskJiraLinkTaskParams.from_dict(data)

                return task_params_type_59
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_60 = CreateClickupTaskTaskParams.from_dict(data)

                return task_params_type_60
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_61 = CreateMotionTaskTaskParams.from_dict(data)

                return task_params_type_61
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_62 = CreateZoomMeetingTaskParams.from_dict(data)

                return task_params_type_62
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_65 = GetPulsesTaskParams.from_dict(data)

                return task_params_type_65
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_66 = GetAlertsTaskParams.from_dict(data)

                return task_params_type_66
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_67 = HttpClientTaskParams.from_dict(data)

                return task_params_type_67
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_68 = InviteToSlackChannelOpsgenieTaskParams.from_dict(data)

                return task_params_type_68
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_69 = InviteToSlackChannelRootlyTaskParams.from_dict(data)

                return task_params_type_69
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_72 = InviteToSlackChannelVictorOpsTaskParams.from_dict(data)

                return task_params_type_72
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_73 = PageOpsgenieOnCallRespondersTaskParams.from_dict(data)

                return task_params_type_73
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_74 = CreateOpsgenieAlertTaskParams.from_dict(data)

                return task_params_type_74
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_75 = UpdateOpsgenieAlertTaskParams.from_dict(data)

                return task_params_type_75
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_76 = UpdateOpsgenieIncidentTaskParams.from_dict(data)

                return task_params_type_76
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_77 = PageRootlyOnCallRespondersTaskParams.from_dict(data)

                return task_params_type_77
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_78 = PagePagerdutyOnCallRespondersTaskParams.from_dict(data)

                return task_params_type_78
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_80 = UpdateVictorOpsIncidentTaskParams.from_dict(data)

                return task_params_type_80
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_81 = PrintTaskParams.from_dict(data)

                return task_params_type_81
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_82 = PublishIncidentTaskParams.from_dict(data)

                return task_params_type_82
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_83 = RedisClientTaskParams.from_dict(data)

                return task_params_type_83
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_84 = RenameSlackChannelTaskParams.from_dict(data)

                return task_params_type_84
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_85 = ChangeSlackChannelPrivacyTaskParams.from_dict(data)

                return task_params_type_85
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_86 = RunCommandHerokuTaskParams.from_dict(data)

                return task_params_type_86
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_87 = SendEmailTaskParams.from_dict(data)

                return task_params_type_87
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_88 = SendDashboardReportTaskParams.from_dict(data)

                return task_params_type_88
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_89 = CreateSlackChannelTaskParams.from_dict(data)

                return task_params_type_89
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_91 = SendSmsTaskParams.from_dict(data)

                return task_params_type_91
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_92 = SendWhatsappMessageTaskParams.from_dict(data)

                return task_params_type_92
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_93 = SnapshotDatadogGraphTaskParams.from_dict(data)

                return task_params_type_93
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_94 = SnapshotGrafanaDashboardTaskParams.from_dict(data)

                return task_params_type_94
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_95 = SnapshotLookerLookTaskParams.from_dict(data)

                return task_params_type_95
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_96 = SnapshotNewRelicGraphTaskParams.from_dict(data)

                return task_params_type_96
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_97 = TweetTwitterMessageTaskParams.from_dict(data)

                return task_params_type_97
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_98 = UpdateAirtableTableRecordTaskParams.from_dict(data)

                return task_params_type_98
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_99 = UpdateAsanaTaskTaskParams.from_dict(data)

                return task_params_type_99
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_100 = UpdateGithubIssueTaskParams.from_dict(data)

                return task_params_type_100
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_101 = UpdateGitlabIssueTaskParams.from_dict(data)

                return task_params_type_101
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_102 = UpdateIncidentTaskParams.from_dict(data)

                return task_params_type_102
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_103 = UpdateIncidentPostmortemTaskParams.from_dict(data)

                return task_params_type_103
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_104 = UpdateJiraIssueTaskParams.from_dict(data)

                return task_params_type_104
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_105 = UpdateLinearIssueTaskParams.from_dict(data)

                return task_params_type_105
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_106 = UpdateServiceNowIncidentTaskParams.from_dict(data)

                return task_params_type_106
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_107 = UpdateShortcutStoryTaskParams.from_dict(data)

                return task_params_type_107
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_108 = UpdateShortcutTaskTaskParams.from_dict(data)

                return task_params_type_108
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_109 = UpdateSlackChannelTopicTaskParams.from_dict(data)

                return task_params_type_109
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_110 = UpdateStatusTaskParams.from_dict(data)

                return task_params_type_110
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_111 = UpdateIncidentStatusTimestampTaskParams.from_dict(data)

                return task_params_type_111
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_112 = UpdateTrelloCardTaskParams.from_dict(data)

                return task_params_type_112
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_113 = UpdateClickupTaskTaskParams.from_dict(data)

                return task_params_type_113
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_114 = UpdateMotionTaskTaskParams.from_dict(data)

                return task_params_type_114
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_115 = UpdateZendeskTicketTaskParams.from_dict(data)

                return task_params_type_115
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_116 = UpdateAttachedAlertsTaskParams.from_dict(data)

                return task_params_type_116
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_117 = TriggerWorkflowTaskParams.from_dict(data)

                return task_params_type_117
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_119 = GeniusCreateOpenaiChatCompletionTaskParams.from_dict(data)

                return task_params_type_119
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_120 = GeniusCreateWatsonxChatCompletionTaskParams.from_dict(data)

                return task_params_type_120
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "AddActionItemTaskParams",
                    "AddRoleTaskParams",
                    "AddTeamTaskParams",
                    "AddToTimelineTaskParams",
                    "ArchiveMicrosoftTeamsChannelsTaskParams",
                    "ArchiveSlackChannelsTaskParams",
                    "AttachDatadogDashboardsTaskParams",
                    "AutoAssignRoleOpsgenieTaskParams",
                    "AutoAssignRoleRootlyTaskParams",
                    "AutoAssignRoleVictorOpsTaskParams",
                    "CallPeopleTaskParams",
                    "ChangeSlackChannelPrivacyTaskParams",
                    "CreateAirtableTableRecordTaskParams",
                    "CreateAsanaSubtaskTaskParams",
                    "CreateAsanaTaskTaskParams",
                    "CreateClickupTaskTaskParams",
                    "CreateConfluencePageTaskParams",
                    "CreateDatadogNotebookTaskParams",
                    "CreateDropboxPaperPageTaskParams",
                    "CreateGithubIssueTaskParams",
                    "CreateGitlabIssueTaskParams",
                    "CreateGoToMeetingTaskParams",
                    "CreateGoogleCalendarEventTaskParams",
                    "CreateGoogleDocsPageTaskParams",
                    "CreateGoogleDocsPermissionsTaskParams",
                    "CreateGoogleMeetingTaskParams",
                    "CreateIncidentPostmortemTaskParams",
                    "CreateIncidentTaskParams",
                    "CreateJiraIssueTaskParams",
                    "CreateJiraSubtaskTaskParams",
                    "CreateLinearIssueCommentTaskParams",
                    "CreateLinearIssueTaskParams",
                    "CreateLinearSubtaskIssueTaskParams",
                    "CreateMicrosoftTeamsChannelTaskParams",
                    "CreateMicrosoftTeamsMeetingTaskParams",
                    "CreateMotionTaskTaskParams",
                    "CreateNotionPageTaskParams",
                    "CreateOpsgenieAlertTaskParams",
                    "CreateOutlookEventTaskParams",
                    "CreatePagerdutyStatusUpdateTaskParams",
                    "CreatePagertreeAlertTaskParams",
                    "CreateQuipPageTaskParams",
                    "CreateServiceNowIncidentTaskParams",
                    "CreateSharepointPageTaskParams",
                    "CreateShortcutTaskTaskParams",
                    "CreateSlackChannelTaskParams",
                    "CreateTrelloCardTaskParams",
                    "CreateWebexMeetingTaskParams",
                    "CreateZendeskJiraLinkTaskParams",
                    "CreateZendeskTicketTaskParams",
                    "CreateZoomMeetingTaskParams",
                    "GeniusCreateOpenaiChatCompletionTaskParams",
                    "GeniusCreateWatsonxChatCompletionTaskParams",
                    "GetAlertsTaskParams",
                    "GetPulsesTaskParams",
                    "HttpClientTaskParams",
                    "InviteToMicrosoftTeamsChannelTaskParams",
                    "InviteToSlackChannelOpsgenieTaskParams",
                    "InviteToSlackChannelRootlyTaskParams",
                    "InviteToSlackChannelVictorOpsTaskParams",
                    "PageOpsgenieOnCallRespondersTaskParams",
                    "PagePagerdutyOnCallRespondersTaskParams",
                    "PageRootlyOnCallRespondersTaskParams",
                    "PrintTaskParams",
                    "PublishIncidentTaskParams",
                    "RedisClientTaskParams",
                    "RemoveGoogleDocsPermissionsTaskParams",
                    "RenameMicrosoftTeamsChannelTaskParams",
                    "RenameSlackChannelTaskParams",
                    "RunCommandHerokuTaskParams",
                    "SendDashboardReportTaskParams",
                    "SendEmailTaskParams",
                    "SendSmsTaskParams",
                    "SendWhatsappMessageTaskParams",
                    "SnapshotDatadogGraphTaskParams",
                    "SnapshotGrafanaDashboardTaskParams",
                    "SnapshotLookerLookTaskParams",
                    "SnapshotNewRelicGraphTaskParams",
                    "TriggerWorkflowTaskParams",
                    "TweetTwitterMessageTaskParams",
                    "UpdateActionItemTaskParams",
                    "UpdateAirtableTableRecordTaskParams",
                    "UpdateAsanaTaskTaskParams",
                    "UpdateAttachedAlertsTaskParams",
                    "UpdateClickupTaskTaskParams",
                    "UpdateGithubIssueTaskParams",
                    "UpdateGitlabIssueTaskParams",
                    "UpdateGoogleCalendarEventTaskParams",
                    "UpdateGoogleDocsPageTaskParams",
                    "UpdateIncidentPostmortemTaskParams",
                    "UpdateIncidentStatusTimestampTaskParams",
                    "UpdateIncidentTaskParams",
                    "UpdateJiraIssueTaskParams",
                    "UpdateLinearIssueTaskParams",
                    "UpdateMotionTaskTaskParams",
                    "UpdateNotionPageTaskParams",
                    "UpdateOpsgenieAlertTaskParams",
                    "UpdateOpsgenieIncidentTaskParams",
                    "UpdatePagerdutyIncidentTaskParams",
                    "UpdatePagertreeAlertTaskParams",
                    "UpdateServiceNowIncidentTaskParams",
                    "UpdateShortcutStoryTaskParams",
                    "UpdateShortcutTaskTaskParams",
                    "UpdateSlackChannelTopicTaskParams",
                    "UpdateStatusTaskParams",
                    "UpdateTrelloCardTaskParams",
                    "UpdateVictorOpsIncidentTaskParams",
                    "UpdateZendeskTicketTaskParams",
                    Any,
                    Unset,
                ],
                data,
            )

        task_params = _parse_task_params(d.pop("task_params", UNSET))

        update_workflow_task_data_attributes = cls(
            name=name,
            position=position,
            skip_on_failure=skip_on_failure,
            enabled=enabled,
            task_params=task_params,
        )

        return update_workflow_task_data_attributes
