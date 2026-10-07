from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_action_item_task_params import AddActionItemTaskParams
    from ..models.add_microsoft_teams_chat_tab_task_params import AddMicrosoftTeamsChatTabTaskParams
    from ..models.add_microsoft_teams_tab_task_params_type_0 import AddMicrosoftTeamsTabTaskParamsType0
    from ..models.add_microsoft_teams_tab_task_params_type_1 import AddMicrosoftTeamsTabTaskParamsType1
    from ..models.add_role_task_params import AddRoleTaskParams
    from ..models.add_slack_bookmark_task_params_type_0 import AddSlackBookmarkTaskParamsType0
    from ..models.add_slack_bookmark_task_params_type_1 import AddSlackBookmarkTaskParamsType1
    from ..models.add_team_task_params import AddTeamTaskParams
    from ..models.add_to_timeline_task_params import AddToTimelineTaskParams
    from ..models.archive_google_chat_spaces_task_params import ArchiveGoogleChatSpacesTaskParams
    from ..models.archive_microsoft_teams_channels_task_params import ArchiveMicrosoftTeamsChannelsTaskParams
    from ..models.archive_slack_channels_task_params import ArchiveSlackChannelsTaskParams
    from ..models.attach_datadog_dashboards_task_params import AttachDatadogDashboardsTaskParams
    from ..models.attach_retrospective_pdf_to_freshservice_ticket_task_params import (
        AttachRetrospectivePdfToFreshserviceTicketTaskParams,
    )
    from ..models.attach_retrospective_pdf_to_jira_issue_task_params import AttachRetrospectivePdfToJiraIssueTaskParams
    from ..models.auto_assign_role_opsgenie_task_params import AutoAssignRoleOpsgenieTaskParams
    from ..models.auto_assign_role_pagerduty_task_params_type_0 import AutoAssignRolePagerdutyTaskParamsType0
    from ..models.auto_assign_role_pagerduty_task_params_type_1 import AutoAssignRolePagerdutyTaskParamsType1
    from ..models.auto_assign_role_rootly_task_params_type_0 import AutoAssignRoleRootlyTaskParamsType0
    from ..models.auto_assign_role_rootly_task_params_type_1 import AutoAssignRoleRootlyTaskParamsType1
    from ..models.auto_assign_role_rootly_task_params_type_2 import AutoAssignRoleRootlyTaskParamsType2
    from ..models.auto_assign_role_rootly_task_params_type_3 import AutoAssignRoleRootlyTaskParamsType3
    from ..models.auto_assign_role_rootly_task_params_type_4 import AutoAssignRoleRootlyTaskParamsType4
    from ..models.auto_assign_role_victor_ops_task_params import AutoAssignRoleVictorOpsTaskParams
    from ..models.call_people_task_params import CallPeopleTaskParams
    from ..models.change_google_chat_space_privacy_task_params import ChangeGoogleChatSpacePrivacyTaskParams
    from ..models.change_slack_channel_privacy_task_params import ChangeSlackChannelPrivacyTaskParams
    from ..models.create_airtable_table_record_task_params import CreateAirtableTableRecordTaskParams
    from ..models.create_anthropic_chat_completion_task_params import CreateAnthropicChatCompletionTaskParams
    from ..models.create_asana_subtask_task_params import CreateAsanaSubtaskTaskParams
    from ..models.create_asana_task_task_params import CreateAsanaTaskTaskParams
    from ..models.create_clickup_task_task_params import CreateClickupTaskTaskParams
    from ..models.create_coda_page_task_params import CreateCodaPageTaskParams
    from ..models.create_confluence_page_task_params import CreateConfluencePageTaskParams
    from ..models.create_datadog_notebook_task_params import CreateDatadogNotebookTaskParams
    from ..models.create_dropbox_paper_page_task_params import CreateDropboxPaperPageTaskParams
    from ..models.create_github_issue_task_params import CreateGithubIssueTaskParams
    from ..models.create_gitlab_issue_task_params import CreateGitlabIssueTaskParams
    from ..models.create_go_to_meeting_task_params import CreateGoToMeetingTaskParams
    from ..models.create_google_calendar_event_task_params import CreateGoogleCalendarEventTaskParams
    from ..models.create_google_chat_space_task_params import CreateGoogleChatSpaceTaskParams
    from ..models.create_google_docs_page_task_params import CreateGoogleDocsPageTaskParams
    from ..models.create_google_docs_permissions_task_params import CreateGoogleDocsPermissionsTaskParams
    from ..models.create_google_gemini_chat_completion_task_params import CreateGoogleGeminiChatCompletionTaskParams
    from ..models.create_google_meeting_task_params import CreateGoogleMeetingTaskParams
    from ..models.create_incident_postmortem_task_params import CreateIncidentPostmortemTaskParams
    from ..models.create_incident_task_params import CreateIncidentTaskParams
    from ..models.create_jira_issue_task_params import CreateJiraIssueTaskParams
    from ..models.create_jira_subtask_task_params import CreateJiraSubtaskTaskParams
    from ..models.create_jsmops_alert_task_params import CreateJsmopsAlertTaskParams
    from ..models.create_linear_issue_comment_task_params import CreateLinearIssueCommentTaskParams
    from ..models.create_linear_issue_task_params import CreateLinearIssueTaskParams
    from ..models.create_linear_subtask_issue_task_params import CreateLinearSubtaskIssueTaskParams
    from ..models.create_microsoft_teams_channel_task_params import CreateMicrosoftTeamsChannelTaskParams
    from ..models.create_microsoft_teams_chat_task_params import CreateMicrosoftTeamsChatTaskParams
    from ..models.create_microsoft_teams_meeting_task_params import CreateMicrosoftTeamsMeetingTaskParams
    from ..models.create_mistral_chat_completion_task_params import CreateMistralChatCompletionTaskParams
    from ..models.create_motion_task_task_params import CreateMotionTaskTaskParams
    from ..models.create_notion_page_task_params import CreateNotionPageTaskParams
    from ..models.create_openai_chat_completion_task_params import CreateOpenaiChatCompletionTaskParams
    from ..models.create_opsgenie_alert_task_params import CreateOpsgenieAlertTaskParams
    from ..models.create_outlook_event_task_params import CreateOutlookEventTaskParams
    from ..models.create_pagerduty_status_update_task_params import CreatePagerdutyStatusUpdateTaskParams
    from ..models.create_pagertree_alert_task_params import CreatePagertreeAlertTaskParams
    from ..models.create_quip_page_task_params import CreateQuipPageTaskParams
    from ..models.create_service_now_incident_task_params import CreateServiceNowIncidentTaskParams
    from ..models.create_sharepoint_page_task_params import CreateSharepointPageTaskParams
    from ..models.create_shortcut_story_task_params_type_0 import CreateShortcutStoryTaskParamsType0
    from ..models.create_shortcut_story_task_params_type_1 import CreateShortcutStoryTaskParamsType1
    from ..models.create_shortcut_task_task_params import CreateShortcutTaskTaskParams
    from ..models.create_slack_canvas_task_params import CreateSlackCanvasTaskParams
    from ..models.create_slack_channel_task_params import CreateSlackChannelTaskParams
    from ..models.create_sub_incident_task_params import CreateSubIncidentTaskParams
    from ..models.create_trello_card_task_params import CreateTrelloCardTaskParams
    from ..models.create_watsonx_chat_completion_task_params import CreateWatsonxChatCompletionTaskParams
    from ..models.create_webex_meeting_task_params import CreateWebexMeetingTaskParams
    from ..models.create_zendesk_jira_link_task_params import CreateZendeskJiraLinkTaskParams
    from ..models.create_zendesk_ticket_task_params import CreateZendeskTicketTaskParams
    from ..models.create_zoom_meeting_task_params import CreateZoomMeetingTaskParams
    from ..models.get_alerts_task_params import GetAlertsTaskParams
    from ..models.get_github_commits_task_params_type_0 import GetGithubCommitsTaskParamsType0
    from ..models.get_github_commits_task_params_type_1 import GetGithubCommitsTaskParamsType1
    from ..models.get_gitlab_commits_task_params_type_0 import GetGitlabCommitsTaskParamsType0
    from ..models.get_gitlab_commits_task_params_type_1 import GetGitlabCommitsTaskParamsType1
    from ..models.get_pulses_task_params import GetPulsesTaskParams
    from ..models.http_client_task_params import HttpClientTaskParams
    from ..models.invite_to_google_chat_space_task_params import InviteToGoogleChatSpaceTaskParams
    from ..models.invite_to_microsoft_teams_channel_rootly_task_params import (
        InviteToMicrosoftTeamsChannelRootlyTaskParams,
    )
    from ..models.invite_to_microsoft_teams_channel_task_params import InviteToMicrosoftTeamsChannelTaskParams
    from ..models.invite_to_slack_channel_opsgenie_task_params import InviteToSlackChannelOpsgenieTaskParams
    from ..models.invite_to_slack_channel_pagerduty_task_params_type_0 import (
        InviteToSlackChannelPagerdutyTaskParamsType0,
    )
    from ..models.invite_to_slack_channel_pagerduty_task_params_type_1 import (
        InviteToSlackChannelPagerdutyTaskParamsType1,
    )
    from ..models.invite_to_slack_channel_rootly_task_params import InviteToSlackChannelRootlyTaskParams
    from ..models.invite_to_slack_channel_task_params_type_0 import InviteToSlackChannelTaskParamsType0
    from ..models.invite_to_slack_channel_task_params_type_1 import InviteToSlackChannelTaskParamsType1
    from ..models.invite_to_slack_channel_task_params_type_2 import InviteToSlackChannelTaskParamsType2
    from ..models.invite_to_slack_channel_victor_ops_task_params import InviteToSlackChannelVictorOpsTaskParams
    from ..models.page_jsmops_on_call_responders_task_params import PageJsmopsOnCallRespondersTaskParams
    from ..models.page_opsgenie_on_call_responders_task_params import PageOpsgenieOnCallRespondersTaskParams
    from ..models.page_pagerduty_on_call_responders_task_params import PagePagerdutyOnCallRespondersTaskParams
    from ..models.page_rootly_on_call_responders_task_params import PageRootlyOnCallRespondersTaskParams
    from ..models.page_victor_ops_on_call_responders_task_params_type_0 import (
        PageVictorOpsOnCallRespondersTaskParamsType0,
    )
    from ..models.page_victor_ops_on_call_responders_task_params_type_1 import (
        PageVictorOpsOnCallRespondersTaskParamsType1,
    )
    from ..models.print_task_params import PrintTaskParams
    from ..models.publish_incident_task_params import PublishIncidentTaskParams
    from ..models.redis_client_task_params import RedisClientTaskParams
    from ..models.remove_from_slack_channel_task_params import RemoveFromSlackChannelTaskParams
    from ..models.remove_google_docs_permissions_task_params import RemoveGoogleDocsPermissionsTaskParams
    from ..models.rename_google_chat_space_task_params import RenameGoogleChatSpaceTaskParams
    from ..models.rename_microsoft_teams_channel_task_params import RenameMicrosoftTeamsChannelTaskParams
    from ..models.rename_slack_channel_task_params import RenameSlackChannelTaskParams
    from ..models.run_command_heroku_task_params import RunCommandHerokuTaskParams
    from ..models.send_dashboard_report_task_params import SendDashboardReportTaskParams
    from ..models.send_email_task_params import SendEmailTaskParams
    from ..models.send_google_chat_attachments_task_params import SendGoogleChatAttachmentsTaskParams
    from ..models.send_google_chat_message_task_params import SendGoogleChatMessageTaskParams
    from ..models.send_microsoft_teams_blocks_task_params_type_0 import SendMicrosoftTeamsBlocksTaskParamsType0
    from ..models.send_microsoft_teams_chat_message_task_params import SendMicrosoftTeamsChatMessageTaskParams
    from ..models.send_microsoft_teams_message_task_params_type_0 import SendMicrosoftTeamsMessageTaskParamsType0
    from ..models.send_slack_blocks_task_params_type_0 import SendSlackBlocksTaskParamsType0
    from ..models.send_slack_blocks_task_params_type_1 import SendSlackBlocksTaskParamsType1
    from ..models.send_slack_blocks_task_params_type_2 import SendSlackBlocksTaskParamsType2
    from ..models.send_slack_message_task_params_type_0 import SendSlackMessageTaskParamsType0
    from ..models.send_slack_message_task_params_type_1 import SendSlackMessageTaskParamsType1
    from ..models.send_slack_message_task_params_type_2 import SendSlackMessageTaskParamsType2
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
    from ..models.update_coda_page_task_params import UpdateCodaPageTaskParams
    from ..models.update_confluence_page_task_params import UpdateConfluencePageTaskParams
    from ..models.update_datadog_notebook_task_params import UpdateDatadogNotebookTaskParams
    from ..models.update_dropbox_paper_page_task_params import UpdateDropboxPaperPageTaskParams
    from ..models.update_github_issue_task_params import UpdateGithubIssueTaskParams
    from ..models.update_gitlab_issue_task_params import UpdateGitlabIssueTaskParams
    from ..models.update_google_calendar_event_task_params import UpdateGoogleCalendarEventTaskParams
    from ..models.update_google_chat_space_description_task_params import UpdateGoogleChatSpaceDescriptionTaskParams
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
    from ..models.update_quip_page_task_params import UpdateQuipPageTaskParams
    from ..models.update_service_now_incident_task_params import UpdateServiceNowIncidentTaskParams
    from ..models.update_sharepoint_page_task_params import UpdateSharepointPageTaskParams
    from ..models.update_shortcut_story_task_params import UpdateShortcutStoryTaskParams
    from ..models.update_shortcut_task_task_params import UpdateShortcutTaskTaskParams
    from ..models.update_slack_canvas_task_params import UpdateSlackCanvasTaskParams
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
        name (str | Unset): Name of the workflow task
        position (int | Unset): The position of the workflow task
        skip_on_failure (bool | Unset): Skip workflow task if any failures
        enabled (bool | Unset): Enable/disable workflow task Default: True.
        task_params (AddActionItemTaskParams | AddMicrosoftTeamsChatTabTaskParams | AddMicrosoftTeamsTabTaskParamsType0
            | AddMicrosoftTeamsTabTaskParamsType1 | AddRoleTaskParams | AddSlackBookmarkTaskParamsType0 |
            AddSlackBookmarkTaskParamsType1 | AddTeamTaskParams | AddToTimelineTaskParams |
            ArchiveGoogleChatSpacesTaskParams | ArchiveMicrosoftTeamsChannelsTaskParams | ArchiveSlackChannelsTaskParams |
            AttachDatadogDashboardsTaskParams | AttachRetrospectivePdfToFreshserviceTicketTaskParams |
            AttachRetrospectivePdfToJiraIssueTaskParams | AutoAssignRoleOpsgenieTaskParams |
            AutoAssignRolePagerdutyTaskParamsType0 | AutoAssignRolePagerdutyTaskParamsType1 |
            AutoAssignRoleRootlyTaskParamsType0 | AutoAssignRoleRootlyTaskParamsType1 | AutoAssignRoleRootlyTaskParamsType2
            | AutoAssignRoleRootlyTaskParamsType3 | AutoAssignRoleRootlyTaskParamsType4 | AutoAssignRoleVictorOpsTaskParams
            | CallPeopleTaskParams | ChangeGoogleChatSpacePrivacyTaskParams | ChangeSlackChannelPrivacyTaskParams |
            CreateAirtableTableRecordTaskParams | CreateAnthropicChatCompletionTaskParams | CreateAsanaSubtaskTaskParams |
            CreateAsanaTaskTaskParams | CreateClickupTaskTaskParams | CreateCodaPageTaskParams |
            CreateConfluencePageTaskParams | CreateDatadogNotebookTaskParams | CreateDropboxPaperPageTaskParams |
            CreateGithubIssueTaskParams | CreateGitlabIssueTaskParams | CreateGoogleCalendarEventTaskParams |
            CreateGoogleChatSpaceTaskParams | CreateGoogleDocsPageTaskParams | CreateGoogleDocsPermissionsTaskParams |
            CreateGoogleGeminiChatCompletionTaskParams | CreateGoogleMeetingTaskParams | CreateGoToMeetingTaskParams |
            CreateIncidentPostmortemTaskParams | CreateIncidentTaskParams | CreateJiraIssueTaskParams |
            CreateJiraSubtaskTaskParams | CreateJsmopsAlertTaskParams | CreateLinearIssueCommentTaskParams |
            CreateLinearIssueTaskParams | CreateLinearSubtaskIssueTaskParams | CreateMicrosoftTeamsChannelTaskParams |
            CreateMicrosoftTeamsChatTaskParams | CreateMicrosoftTeamsMeetingTaskParams |
            CreateMistralChatCompletionTaskParams | CreateMotionTaskTaskParams | CreateNotionPageTaskParams |
            CreateOpenaiChatCompletionTaskParams | CreateOpsgenieAlertTaskParams | CreateOutlookEventTaskParams |
            CreatePagerdutyStatusUpdateTaskParams | CreatePagertreeAlertTaskParams | CreateQuipPageTaskParams |
            CreateServiceNowIncidentTaskParams | CreateSharepointPageTaskParams | CreateShortcutStoryTaskParamsType0 |
            CreateShortcutStoryTaskParamsType1 | CreateShortcutTaskTaskParams | CreateSlackCanvasTaskParams |
            CreateSlackChannelTaskParams | CreateSubIncidentTaskParams | CreateTrelloCardTaskParams |
            CreateWatsonxChatCompletionTaskParams | CreateWebexMeetingTaskParams | CreateZendeskJiraLinkTaskParams |
            CreateZendeskTicketTaskParams | CreateZoomMeetingTaskParams | GetAlertsTaskParams |
            GetGithubCommitsTaskParamsType0 | GetGithubCommitsTaskParamsType1 | GetGitlabCommitsTaskParamsType0 |
            GetGitlabCommitsTaskParamsType1 | GetPulsesTaskParams | HttpClientTaskParams | InviteToGoogleChatSpaceTaskParams
            | InviteToMicrosoftTeamsChannelRootlyTaskParams | InviteToMicrosoftTeamsChannelTaskParams |
            InviteToSlackChannelOpsgenieTaskParams | InviteToSlackChannelPagerdutyTaskParamsType0 |
            InviteToSlackChannelPagerdutyTaskParamsType1 | InviteToSlackChannelRootlyTaskParams |
            InviteToSlackChannelTaskParamsType0 | InviteToSlackChannelTaskParamsType1 | InviteToSlackChannelTaskParamsType2
            | InviteToSlackChannelVictorOpsTaskParams | PageJsmopsOnCallRespondersTaskParams |
            PageOpsgenieOnCallRespondersTaskParams | PagePagerdutyOnCallRespondersTaskParams |
            PageRootlyOnCallRespondersTaskParams | PageVictorOpsOnCallRespondersTaskParamsType0 |
            PageVictorOpsOnCallRespondersTaskParamsType1 | PrintTaskParams | PublishIncidentTaskParams |
            RedisClientTaskParams | RemoveFromSlackChannelTaskParams | RemoveGoogleDocsPermissionsTaskParams |
            RenameGoogleChatSpaceTaskParams | RenameMicrosoftTeamsChannelTaskParams | RenameSlackChannelTaskParams |
            RunCommandHerokuTaskParams | SendDashboardReportTaskParams | SendEmailTaskParams |
            SendGoogleChatAttachmentsTaskParams | SendGoogleChatMessageTaskParams | SendMicrosoftTeamsBlocksTaskParamsType0
            | SendMicrosoftTeamsChatMessageTaskParams | SendMicrosoftTeamsMessageTaskParamsType0 |
            SendSlackBlocksTaskParamsType0 | SendSlackBlocksTaskParamsType1 | SendSlackBlocksTaskParamsType2 |
            SendSlackMessageTaskParamsType0 | SendSlackMessageTaskParamsType1 | SendSlackMessageTaskParamsType2 |
            SendSmsTaskParams | SendWhatsappMessageTaskParams | SnapshotDatadogGraphTaskParams |
            SnapshotGrafanaDashboardTaskParams | SnapshotLookerLookTaskParams | SnapshotNewRelicGraphTaskParams |
            TriggerWorkflowTaskParams | TweetTwitterMessageTaskParams | Unset | UpdateActionItemTaskParams |
            UpdateAirtableTableRecordTaskParams | UpdateAsanaTaskTaskParams | UpdateAttachedAlertsTaskParams |
            UpdateClickupTaskTaskParams | UpdateCodaPageTaskParams | UpdateConfluencePageTaskParams |
            UpdateDatadogNotebookTaskParams | UpdateDropboxPaperPageTaskParams | UpdateGithubIssueTaskParams |
            UpdateGitlabIssueTaskParams | UpdateGoogleCalendarEventTaskParams | UpdateGoogleChatSpaceDescriptionTaskParams |
            UpdateGoogleDocsPageTaskParams | UpdateIncidentPostmortemTaskParams | UpdateIncidentStatusTimestampTaskParams |
            UpdateIncidentTaskParams | UpdateJiraIssueTaskParams | UpdateLinearIssueTaskParams | UpdateMotionTaskTaskParams
            | UpdateNotionPageTaskParams | UpdateOpsgenieAlertTaskParams | UpdateOpsgenieIncidentTaskParams |
            UpdatePagerdutyIncidentTaskParams | UpdatePagertreeAlertTaskParams | UpdateQuipPageTaskParams |
            UpdateServiceNowIncidentTaskParams | UpdateSharepointPageTaskParams | UpdateShortcutStoryTaskParams |
            UpdateShortcutTaskTaskParams | UpdateSlackCanvasTaskParams | UpdateSlackChannelTopicTaskParams |
            UpdateStatusTaskParams | UpdateTrelloCardTaskParams | UpdateVictorOpsIncidentTaskParams |
            UpdateZendeskTicketTaskParams):
    """

    name: str | Unset = UNSET
    position: int | Unset = UNSET
    skip_on_failure: bool | Unset = UNSET
    enabled: bool | Unset = True
    task_params: (
        AddActionItemTaskParams
        | AddMicrosoftTeamsChatTabTaskParams
        | AddMicrosoftTeamsTabTaskParamsType0
        | AddMicrosoftTeamsTabTaskParamsType1
        | AddRoleTaskParams
        | AddSlackBookmarkTaskParamsType0
        | AddSlackBookmarkTaskParamsType1
        | AddTeamTaskParams
        | AddToTimelineTaskParams
        | ArchiveGoogleChatSpacesTaskParams
        | ArchiveMicrosoftTeamsChannelsTaskParams
        | ArchiveSlackChannelsTaskParams
        | AttachDatadogDashboardsTaskParams
        | AttachRetrospectivePdfToFreshserviceTicketTaskParams
        | AttachRetrospectivePdfToJiraIssueTaskParams
        | AutoAssignRoleOpsgenieTaskParams
        | AutoAssignRolePagerdutyTaskParamsType0
        | AutoAssignRolePagerdutyTaskParamsType1
        | AutoAssignRoleRootlyTaskParamsType0
        | AutoAssignRoleRootlyTaskParamsType1
        | AutoAssignRoleRootlyTaskParamsType2
        | AutoAssignRoleRootlyTaskParamsType3
        | AutoAssignRoleRootlyTaskParamsType4
        | AutoAssignRoleVictorOpsTaskParams
        | CallPeopleTaskParams
        | ChangeGoogleChatSpacePrivacyTaskParams
        | ChangeSlackChannelPrivacyTaskParams
        | CreateAirtableTableRecordTaskParams
        | CreateAnthropicChatCompletionTaskParams
        | CreateAsanaSubtaskTaskParams
        | CreateAsanaTaskTaskParams
        | CreateClickupTaskTaskParams
        | CreateCodaPageTaskParams
        | CreateConfluencePageTaskParams
        | CreateDatadogNotebookTaskParams
        | CreateDropboxPaperPageTaskParams
        | CreateGithubIssueTaskParams
        | CreateGitlabIssueTaskParams
        | CreateGoogleCalendarEventTaskParams
        | CreateGoogleChatSpaceTaskParams
        | CreateGoogleDocsPageTaskParams
        | CreateGoogleDocsPermissionsTaskParams
        | CreateGoogleGeminiChatCompletionTaskParams
        | CreateGoogleMeetingTaskParams
        | CreateGoToMeetingTaskParams
        | CreateIncidentPostmortemTaskParams
        | CreateIncidentTaskParams
        | CreateJiraIssueTaskParams
        | CreateJiraSubtaskTaskParams
        | CreateJsmopsAlertTaskParams
        | CreateLinearIssueCommentTaskParams
        | CreateLinearIssueTaskParams
        | CreateLinearSubtaskIssueTaskParams
        | CreateMicrosoftTeamsChannelTaskParams
        | CreateMicrosoftTeamsChatTaskParams
        | CreateMicrosoftTeamsMeetingTaskParams
        | CreateMistralChatCompletionTaskParams
        | CreateMotionTaskTaskParams
        | CreateNotionPageTaskParams
        | CreateOpenaiChatCompletionTaskParams
        | CreateOpsgenieAlertTaskParams
        | CreateOutlookEventTaskParams
        | CreatePagerdutyStatusUpdateTaskParams
        | CreatePagertreeAlertTaskParams
        | CreateQuipPageTaskParams
        | CreateServiceNowIncidentTaskParams
        | CreateSharepointPageTaskParams
        | CreateShortcutStoryTaskParamsType0
        | CreateShortcutStoryTaskParamsType1
        | CreateShortcutTaskTaskParams
        | CreateSlackCanvasTaskParams
        | CreateSlackChannelTaskParams
        | CreateSubIncidentTaskParams
        | CreateTrelloCardTaskParams
        | CreateWatsonxChatCompletionTaskParams
        | CreateWebexMeetingTaskParams
        | CreateZendeskJiraLinkTaskParams
        | CreateZendeskTicketTaskParams
        | CreateZoomMeetingTaskParams
        | GetAlertsTaskParams
        | GetGithubCommitsTaskParamsType0
        | GetGithubCommitsTaskParamsType1
        | GetGitlabCommitsTaskParamsType0
        | GetGitlabCommitsTaskParamsType1
        | GetPulsesTaskParams
        | HttpClientTaskParams
        | InviteToGoogleChatSpaceTaskParams
        | InviteToMicrosoftTeamsChannelRootlyTaskParams
        | InviteToMicrosoftTeamsChannelTaskParams
        | InviteToSlackChannelOpsgenieTaskParams
        | InviteToSlackChannelPagerdutyTaskParamsType0
        | InviteToSlackChannelPagerdutyTaskParamsType1
        | InviteToSlackChannelRootlyTaskParams
        | InviteToSlackChannelTaskParamsType0
        | InviteToSlackChannelTaskParamsType1
        | InviteToSlackChannelTaskParamsType2
        | InviteToSlackChannelVictorOpsTaskParams
        | PageJsmopsOnCallRespondersTaskParams
        | PageOpsgenieOnCallRespondersTaskParams
        | PagePagerdutyOnCallRespondersTaskParams
        | PageRootlyOnCallRespondersTaskParams
        | PageVictorOpsOnCallRespondersTaskParamsType0
        | PageVictorOpsOnCallRespondersTaskParamsType1
        | PrintTaskParams
        | PublishIncidentTaskParams
        | RedisClientTaskParams
        | RemoveFromSlackChannelTaskParams
        | RemoveGoogleDocsPermissionsTaskParams
        | RenameGoogleChatSpaceTaskParams
        | RenameMicrosoftTeamsChannelTaskParams
        | RenameSlackChannelTaskParams
        | RunCommandHerokuTaskParams
        | SendDashboardReportTaskParams
        | SendEmailTaskParams
        | SendGoogleChatAttachmentsTaskParams
        | SendGoogleChatMessageTaskParams
        | SendMicrosoftTeamsBlocksTaskParamsType0
        | SendMicrosoftTeamsChatMessageTaskParams
        | SendMicrosoftTeamsMessageTaskParamsType0
        | SendSlackBlocksTaskParamsType0
        | SendSlackBlocksTaskParamsType1
        | SendSlackBlocksTaskParamsType2
        | SendSlackMessageTaskParamsType0
        | SendSlackMessageTaskParamsType1
        | SendSlackMessageTaskParamsType2
        | SendSmsTaskParams
        | SendWhatsappMessageTaskParams
        | SnapshotDatadogGraphTaskParams
        | SnapshotGrafanaDashboardTaskParams
        | SnapshotLookerLookTaskParams
        | SnapshotNewRelicGraphTaskParams
        | TriggerWorkflowTaskParams
        | TweetTwitterMessageTaskParams
        | Unset
        | UpdateActionItemTaskParams
        | UpdateAirtableTableRecordTaskParams
        | UpdateAsanaTaskTaskParams
        | UpdateAttachedAlertsTaskParams
        | UpdateClickupTaskTaskParams
        | UpdateCodaPageTaskParams
        | UpdateConfluencePageTaskParams
        | UpdateDatadogNotebookTaskParams
        | UpdateDropboxPaperPageTaskParams
        | UpdateGithubIssueTaskParams
        | UpdateGitlabIssueTaskParams
        | UpdateGoogleCalendarEventTaskParams
        | UpdateGoogleChatSpaceDescriptionTaskParams
        | UpdateGoogleDocsPageTaskParams
        | UpdateIncidentPostmortemTaskParams
        | UpdateIncidentStatusTimestampTaskParams
        | UpdateIncidentTaskParams
        | UpdateJiraIssueTaskParams
        | UpdateLinearIssueTaskParams
        | UpdateMotionTaskTaskParams
        | UpdateNotionPageTaskParams
        | UpdateOpsgenieAlertTaskParams
        | UpdateOpsgenieIncidentTaskParams
        | UpdatePagerdutyIncidentTaskParams
        | UpdatePagertreeAlertTaskParams
        | UpdateQuipPageTaskParams
        | UpdateServiceNowIncidentTaskParams
        | UpdateSharepointPageTaskParams
        | UpdateShortcutStoryTaskParams
        | UpdateShortcutTaskTaskParams
        | UpdateSlackCanvasTaskParams
        | UpdateSlackChannelTopicTaskParams
        | UpdateStatusTaskParams
        | UpdateTrelloCardTaskParams
        | UpdateVictorOpsIncidentTaskParams
        | UpdateZendeskTicketTaskParams
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_action_item_task_params import AddActionItemTaskParams
        from ..models.add_microsoft_teams_chat_tab_task_params import AddMicrosoftTeamsChatTabTaskParams
        from ..models.add_microsoft_teams_tab_task_params_type_0 import AddMicrosoftTeamsTabTaskParamsType0
        from ..models.add_microsoft_teams_tab_task_params_type_1 import AddMicrosoftTeamsTabTaskParamsType1
        from ..models.add_role_task_params import AddRoleTaskParams
        from ..models.add_slack_bookmark_task_params_type_0 import AddSlackBookmarkTaskParamsType0
        from ..models.add_slack_bookmark_task_params_type_1 import AddSlackBookmarkTaskParamsType1
        from ..models.add_team_task_params import AddTeamTaskParams
        from ..models.add_to_timeline_task_params import AddToTimelineTaskParams
        from ..models.archive_google_chat_spaces_task_params import ArchiveGoogleChatSpacesTaskParams
        from ..models.archive_microsoft_teams_channels_task_params import ArchiveMicrosoftTeamsChannelsTaskParams
        from ..models.archive_slack_channels_task_params import ArchiveSlackChannelsTaskParams
        from ..models.attach_datadog_dashboards_task_params import AttachDatadogDashboardsTaskParams
        from ..models.attach_retrospective_pdf_to_freshservice_ticket_task_params import (
            AttachRetrospectivePdfToFreshserviceTicketTaskParams,
        )
        from ..models.attach_retrospective_pdf_to_jira_issue_task_params import (
            AttachRetrospectivePdfToJiraIssueTaskParams,
        )
        from ..models.auto_assign_role_opsgenie_task_params import AutoAssignRoleOpsgenieTaskParams
        from ..models.auto_assign_role_pagerduty_task_params_type_0 import AutoAssignRolePagerdutyTaskParamsType0
        from ..models.auto_assign_role_pagerduty_task_params_type_1 import AutoAssignRolePagerdutyTaskParamsType1
        from ..models.auto_assign_role_rootly_task_params_type_0 import AutoAssignRoleRootlyTaskParamsType0
        from ..models.auto_assign_role_rootly_task_params_type_1 import AutoAssignRoleRootlyTaskParamsType1
        from ..models.auto_assign_role_rootly_task_params_type_2 import AutoAssignRoleRootlyTaskParamsType2
        from ..models.auto_assign_role_rootly_task_params_type_3 import AutoAssignRoleRootlyTaskParamsType3
        from ..models.auto_assign_role_rootly_task_params_type_4 import AutoAssignRoleRootlyTaskParamsType4
        from ..models.auto_assign_role_victor_ops_task_params import AutoAssignRoleVictorOpsTaskParams
        from ..models.call_people_task_params import CallPeopleTaskParams
        from ..models.change_google_chat_space_privacy_task_params import ChangeGoogleChatSpacePrivacyTaskParams
        from ..models.change_slack_channel_privacy_task_params import ChangeSlackChannelPrivacyTaskParams
        from ..models.create_airtable_table_record_task_params import CreateAirtableTableRecordTaskParams
        from ..models.create_asana_subtask_task_params import CreateAsanaSubtaskTaskParams
        from ..models.create_asana_task_task_params import CreateAsanaTaskTaskParams
        from ..models.create_clickup_task_task_params import CreateClickupTaskTaskParams
        from ..models.create_coda_page_task_params import CreateCodaPageTaskParams
        from ..models.create_confluence_page_task_params import CreateConfluencePageTaskParams
        from ..models.create_datadog_notebook_task_params import CreateDatadogNotebookTaskParams
        from ..models.create_dropbox_paper_page_task_params import CreateDropboxPaperPageTaskParams
        from ..models.create_github_issue_task_params import CreateGithubIssueTaskParams
        from ..models.create_gitlab_issue_task_params import CreateGitlabIssueTaskParams
        from ..models.create_go_to_meeting_task_params import CreateGoToMeetingTaskParams
        from ..models.create_google_calendar_event_task_params import CreateGoogleCalendarEventTaskParams
        from ..models.create_google_chat_space_task_params import CreateGoogleChatSpaceTaskParams
        from ..models.create_google_docs_page_task_params import CreateGoogleDocsPageTaskParams
        from ..models.create_google_docs_permissions_task_params import CreateGoogleDocsPermissionsTaskParams
        from ..models.create_google_gemini_chat_completion_task_params import CreateGoogleGeminiChatCompletionTaskParams
        from ..models.create_google_meeting_task_params import CreateGoogleMeetingTaskParams
        from ..models.create_incident_postmortem_task_params import CreateIncidentPostmortemTaskParams
        from ..models.create_incident_task_params import CreateIncidentTaskParams
        from ..models.create_jira_issue_task_params import CreateJiraIssueTaskParams
        from ..models.create_jira_subtask_task_params import CreateJiraSubtaskTaskParams
        from ..models.create_jsmops_alert_task_params import CreateJsmopsAlertTaskParams
        from ..models.create_linear_issue_comment_task_params import CreateLinearIssueCommentTaskParams
        from ..models.create_linear_issue_task_params import CreateLinearIssueTaskParams
        from ..models.create_linear_subtask_issue_task_params import CreateLinearSubtaskIssueTaskParams
        from ..models.create_microsoft_teams_channel_task_params import CreateMicrosoftTeamsChannelTaskParams
        from ..models.create_microsoft_teams_chat_task_params import CreateMicrosoftTeamsChatTaskParams
        from ..models.create_microsoft_teams_meeting_task_params import CreateMicrosoftTeamsMeetingTaskParams
        from ..models.create_mistral_chat_completion_task_params import CreateMistralChatCompletionTaskParams
        from ..models.create_motion_task_task_params import CreateMotionTaskTaskParams
        from ..models.create_notion_page_task_params import CreateNotionPageTaskParams
        from ..models.create_openai_chat_completion_task_params import CreateOpenaiChatCompletionTaskParams
        from ..models.create_opsgenie_alert_task_params import CreateOpsgenieAlertTaskParams
        from ..models.create_outlook_event_task_params import CreateOutlookEventTaskParams
        from ..models.create_pagerduty_status_update_task_params import CreatePagerdutyStatusUpdateTaskParams
        from ..models.create_pagertree_alert_task_params import CreatePagertreeAlertTaskParams
        from ..models.create_quip_page_task_params import CreateQuipPageTaskParams
        from ..models.create_service_now_incident_task_params import CreateServiceNowIncidentTaskParams
        from ..models.create_sharepoint_page_task_params import CreateSharepointPageTaskParams
        from ..models.create_shortcut_story_task_params_type_0 import CreateShortcutStoryTaskParamsType0
        from ..models.create_shortcut_story_task_params_type_1 import CreateShortcutStoryTaskParamsType1
        from ..models.create_shortcut_task_task_params import CreateShortcutTaskTaskParams
        from ..models.create_slack_canvas_task_params import CreateSlackCanvasTaskParams
        from ..models.create_slack_channel_task_params import CreateSlackChannelTaskParams
        from ..models.create_sub_incident_task_params import CreateSubIncidentTaskParams
        from ..models.create_trello_card_task_params import CreateTrelloCardTaskParams
        from ..models.create_watsonx_chat_completion_task_params import CreateWatsonxChatCompletionTaskParams
        from ..models.create_webex_meeting_task_params import CreateWebexMeetingTaskParams
        from ..models.create_zendesk_jira_link_task_params import CreateZendeskJiraLinkTaskParams
        from ..models.create_zendesk_ticket_task_params import CreateZendeskTicketTaskParams
        from ..models.create_zoom_meeting_task_params import CreateZoomMeetingTaskParams
        from ..models.get_alerts_task_params import GetAlertsTaskParams
        from ..models.get_github_commits_task_params_type_0 import GetGithubCommitsTaskParamsType0
        from ..models.get_github_commits_task_params_type_1 import GetGithubCommitsTaskParamsType1
        from ..models.get_gitlab_commits_task_params_type_0 import GetGitlabCommitsTaskParamsType0
        from ..models.get_gitlab_commits_task_params_type_1 import GetGitlabCommitsTaskParamsType1
        from ..models.get_pulses_task_params import GetPulsesTaskParams
        from ..models.http_client_task_params import HttpClientTaskParams
        from ..models.invite_to_google_chat_space_task_params import InviteToGoogleChatSpaceTaskParams
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params import (
            InviteToMicrosoftTeamsChannelRootlyTaskParams,
        )
        from ..models.invite_to_microsoft_teams_channel_task_params import InviteToMicrosoftTeamsChannelTaskParams
        from ..models.invite_to_slack_channel_opsgenie_task_params import InviteToSlackChannelOpsgenieTaskParams
        from ..models.invite_to_slack_channel_pagerduty_task_params_type_0 import (
            InviteToSlackChannelPagerdutyTaskParamsType0,
        )
        from ..models.invite_to_slack_channel_pagerduty_task_params_type_1 import (
            InviteToSlackChannelPagerdutyTaskParamsType1,
        )
        from ..models.invite_to_slack_channel_rootly_task_params import InviteToSlackChannelRootlyTaskParams
        from ..models.invite_to_slack_channel_task_params_type_0 import InviteToSlackChannelTaskParamsType0
        from ..models.invite_to_slack_channel_task_params_type_1 import InviteToSlackChannelTaskParamsType1
        from ..models.invite_to_slack_channel_task_params_type_2 import InviteToSlackChannelTaskParamsType2
        from ..models.invite_to_slack_channel_victor_ops_task_params import InviteToSlackChannelVictorOpsTaskParams
        from ..models.page_jsmops_on_call_responders_task_params import PageJsmopsOnCallRespondersTaskParams
        from ..models.page_opsgenie_on_call_responders_task_params import PageOpsgenieOnCallRespondersTaskParams
        from ..models.page_pagerduty_on_call_responders_task_params import PagePagerdutyOnCallRespondersTaskParams
        from ..models.page_rootly_on_call_responders_task_params import PageRootlyOnCallRespondersTaskParams
        from ..models.page_victor_ops_on_call_responders_task_params_type_0 import (
            PageVictorOpsOnCallRespondersTaskParamsType0,
        )
        from ..models.page_victor_ops_on_call_responders_task_params_type_1 import (
            PageVictorOpsOnCallRespondersTaskParamsType1,
        )
        from ..models.print_task_params import PrintTaskParams
        from ..models.publish_incident_task_params import PublishIncidentTaskParams
        from ..models.redis_client_task_params import RedisClientTaskParams
        from ..models.remove_from_slack_channel_task_params import RemoveFromSlackChannelTaskParams
        from ..models.remove_google_docs_permissions_task_params import RemoveGoogleDocsPermissionsTaskParams
        from ..models.rename_google_chat_space_task_params import RenameGoogleChatSpaceTaskParams
        from ..models.rename_microsoft_teams_channel_task_params import RenameMicrosoftTeamsChannelTaskParams
        from ..models.rename_slack_channel_task_params import RenameSlackChannelTaskParams
        from ..models.run_command_heroku_task_params import RunCommandHerokuTaskParams
        from ..models.send_dashboard_report_task_params import SendDashboardReportTaskParams
        from ..models.send_email_task_params import SendEmailTaskParams
        from ..models.send_google_chat_attachments_task_params import SendGoogleChatAttachmentsTaskParams
        from ..models.send_google_chat_message_task_params import SendGoogleChatMessageTaskParams
        from ..models.send_microsoft_teams_blocks_task_params_type_0 import SendMicrosoftTeamsBlocksTaskParamsType0
        from ..models.send_microsoft_teams_chat_message_task_params import SendMicrosoftTeamsChatMessageTaskParams
        from ..models.send_microsoft_teams_message_task_params_type_0 import SendMicrosoftTeamsMessageTaskParamsType0
        from ..models.send_slack_blocks_task_params_type_0 import SendSlackBlocksTaskParamsType0
        from ..models.send_slack_blocks_task_params_type_1 import SendSlackBlocksTaskParamsType1
        from ..models.send_slack_blocks_task_params_type_2 import SendSlackBlocksTaskParamsType2
        from ..models.send_slack_message_task_params_type_0 import SendSlackMessageTaskParamsType0
        from ..models.send_slack_message_task_params_type_1 import SendSlackMessageTaskParamsType1
        from ..models.send_slack_message_task_params_type_2 import SendSlackMessageTaskParamsType2
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
        from ..models.update_coda_page_task_params import UpdateCodaPageTaskParams
        from ..models.update_confluence_page_task_params import UpdateConfluencePageTaskParams
        from ..models.update_datadog_notebook_task_params import UpdateDatadogNotebookTaskParams
        from ..models.update_dropbox_paper_page_task_params import UpdateDropboxPaperPageTaskParams
        from ..models.update_github_issue_task_params import UpdateGithubIssueTaskParams
        from ..models.update_gitlab_issue_task_params import UpdateGitlabIssueTaskParams
        from ..models.update_google_calendar_event_task_params import UpdateGoogleCalendarEventTaskParams
        from ..models.update_google_chat_space_description_task_params import UpdateGoogleChatSpaceDescriptionTaskParams
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
        from ..models.update_quip_page_task_params import UpdateQuipPageTaskParams
        from ..models.update_service_now_incident_task_params import UpdateServiceNowIncidentTaskParams
        from ..models.update_sharepoint_page_task_params import UpdateSharepointPageTaskParams
        from ..models.update_shortcut_story_task_params import UpdateShortcutStoryTaskParams
        from ..models.update_shortcut_task_task_params import UpdateShortcutTaskTaskParams
        from ..models.update_slack_canvas_task_params import UpdateSlackCanvasTaskParams
        from ..models.update_slack_channel_topic_task_params import UpdateSlackChannelTopicTaskParams
        from ..models.update_status_task_params import UpdateStatusTaskParams
        from ..models.update_trello_card_task_params import UpdateTrelloCardTaskParams
        from ..models.update_victor_ops_incident_task_params import UpdateVictorOpsIncidentTaskParams
        from ..models.update_zendesk_ticket_task_params import UpdateZendeskTicketTaskParams

        name = self.name

        position = self.position

        skip_on_failure = self.skip_on_failure

        enabled = self.enabled

        task_params: dict[str, Any] | Unset
        if isinstance(self.task_params, Unset):
            task_params = UNSET
        elif isinstance(self.task_params, AddActionItemTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateActionItemTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddRoleTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddSlackBookmarkTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddSlackBookmarkTaskParamsType1):
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
        elif isinstance(self.task_params, AutoAssignRoleRootlyTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRoleRootlyTaskParamsType1):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRoleRootlyTaskParamsType2):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRoleRootlyTaskParamsType3):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRoleRootlyTaskParamsType4):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRolePagerdutyTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AutoAssignRolePagerdutyTaskParamsType1):
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
        elif isinstance(self.task_params, CreateCodaPageTaskParams):
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
        elif isinstance(self.task_params, UpdateCodaPageTaskParams):
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
        elif isinstance(self.task_params, CreateSubIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateIncidentPostmortemTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateJiraIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateJiraSubtaskTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AttachRetrospectivePdfToJiraIssueTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AttachRetrospectivePdfToFreshserviceTicketTaskParams):
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
        elif isinstance(self.task_params, CreateMicrosoftTeamsChatTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddMicrosoftTeamsTabTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddMicrosoftTeamsTabTaskParamsType1):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, AddMicrosoftTeamsChatTabTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGoogleChatSpaceTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendGoogleChatMessageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendGoogleChatAttachmentsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToGoogleChatSpaceTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, ArchiveGoogleChatSpacesTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, RenameGoogleChatSpaceTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateGoogleChatSpaceDescriptionTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, ChangeGoogleChatSpacePrivacyTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, ArchiveMicrosoftTeamsChannelsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, RenameMicrosoftTeamsChannelTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToMicrosoftTeamsChannelTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateNotionPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendMicrosoftTeamsMessageTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendMicrosoftTeamsChatMessageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendMicrosoftTeamsBlocksTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateNotionPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateQuipPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateConfluencePageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateSharepointPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateDropboxPaperPageTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateDatadogNotebookTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateServiceNowIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateShortcutStoryTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateShortcutStoryTaskParamsType1):
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
        elif isinstance(self.task_params, GetGithubCommitsTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, GetGithubCommitsTaskParamsType1):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, GetGitlabCommitsTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, GetGitlabCommitsTaskParamsType1):
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
        elif isinstance(self.task_params, InviteToMicrosoftTeamsChannelRootlyTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelPagerdutyTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelPagerdutyTaskParamsType1):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelTaskParamsType1):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelTaskParamsType2):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, InviteToSlackChannelVictorOpsTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PageOpsgenieOnCallRespondersTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateOpsgenieAlertTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateJsmopsAlertTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PageJsmopsOnCallRespondersTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateOpsgenieAlertTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, UpdateOpsgenieIncidentTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PageRootlyOnCallRespondersTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PagePagerdutyOnCallRespondersTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PageVictorOpsOnCallRespondersTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, PageVictorOpsOnCallRespondersTaskParamsType1):
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
        elif isinstance(self.task_params, RemoveFromSlackChannelTaskParams):
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
        elif isinstance(self.task_params, CreateSlackCanvasTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendSlackMessageTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendSlackMessageTaskParamsType1):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendSlackMessageTaskParamsType2):
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
        elif isinstance(self.task_params, UpdateSlackCanvasTaskParams):
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
        elif isinstance(self.task_params, SendSlackBlocksTaskParamsType0):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendSlackBlocksTaskParamsType1):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, SendSlackBlocksTaskParamsType2):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateOpenaiChatCompletionTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateWatsonxChatCompletionTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateGoogleGeminiChatCompletionTaskParams):
            task_params = self.task_params.to_dict()
        elif isinstance(self.task_params, CreateMistralChatCompletionTaskParams):
            task_params = self.task_params.to_dict()
        else:
            task_params = self.task_params.to_dict()

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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_action_item_task_params import AddActionItemTaskParams
        from ..models.add_microsoft_teams_chat_tab_task_params import AddMicrosoftTeamsChatTabTaskParams
        from ..models.add_microsoft_teams_tab_task_params_type_0 import AddMicrosoftTeamsTabTaskParamsType0
        from ..models.add_microsoft_teams_tab_task_params_type_1 import AddMicrosoftTeamsTabTaskParamsType1
        from ..models.add_role_task_params import AddRoleTaskParams
        from ..models.add_slack_bookmark_task_params_type_0 import AddSlackBookmarkTaskParamsType0
        from ..models.add_slack_bookmark_task_params_type_1 import AddSlackBookmarkTaskParamsType1
        from ..models.add_team_task_params import AddTeamTaskParams
        from ..models.add_to_timeline_task_params import AddToTimelineTaskParams
        from ..models.archive_google_chat_spaces_task_params import ArchiveGoogleChatSpacesTaskParams
        from ..models.archive_microsoft_teams_channels_task_params import ArchiveMicrosoftTeamsChannelsTaskParams
        from ..models.archive_slack_channels_task_params import ArchiveSlackChannelsTaskParams
        from ..models.attach_datadog_dashboards_task_params import AttachDatadogDashboardsTaskParams
        from ..models.attach_retrospective_pdf_to_freshservice_ticket_task_params import (
            AttachRetrospectivePdfToFreshserviceTicketTaskParams,
        )
        from ..models.attach_retrospective_pdf_to_jira_issue_task_params import (
            AttachRetrospectivePdfToJiraIssueTaskParams,
        )
        from ..models.auto_assign_role_opsgenie_task_params import AutoAssignRoleOpsgenieTaskParams
        from ..models.auto_assign_role_pagerduty_task_params_type_0 import AutoAssignRolePagerdutyTaskParamsType0
        from ..models.auto_assign_role_pagerduty_task_params_type_1 import AutoAssignRolePagerdutyTaskParamsType1
        from ..models.auto_assign_role_rootly_task_params_type_0 import AutoAssignRoleRootlyTaskParamsType0
        from ..models.auto_assign_role_rootly_task_params_type_1 import AutoAssignRoleRootlyTaskParamsType1
        from ..models.auto_assign_role_rootly_task_params_type_2 import AutoAssignRoleRootlyTaskParamsType2
        from ..models.auto_assign_role_rootly_task_params_type_3 import AutoAssignRoleRootlyTaskParamsType3
        from ..models.auto_assign_role_rootly_task_params_type_4 import AutoAssignRoleRootlyTaskParamsType4
        from ..models.auto_assign_role_victor_ops_task_params import AutoAssignRoleVictorOpsTaskParams
        from ..models.call_people_task_params import CallPeopleTaskParams
        from ..models.change_google_chat_space_privacy_task_params import ChangeGoogleChatSpacePrivacyTaskParams
        from ..models.change_slack_channel_privacy_task_params import ChangeSlackChannelPrivacyTaskParams
        from ..models.create_airtable_table_record_task_params import CreateAirtableTableRecordTaskParams
        from ..models.create_anthropic_chat_completion_task_params import CreateAnthropicChatCompletionTaskParams
        from ..models.create_asana_subtask_task_params import CreateAsanaSubtaskTaskParams
        from ..models.create_asana_task_task_params import CreateAsanaTaskTaskParams
        from ..models.create_clickup_task_task_params import CreateClickupTaskTaskParams
        from ..models.create_coda_page_task_params import CreateCodaPageTaskParams
        from ..models.create_confluence_page_task_params import CreateConfluencePageTaskParams
        from ..models.create_datadog_notebook_task_params import CreateDatadogNotebookTaskParams
        from ..models.create_dropbox_paper_page_task_params import CreateDropboxPaperPageTaskParams
        from ..models.create_github_issue_task_params import CreateGithubIssueTaskParams
        from ..models.create_gitlab_issue_task_params import CreateGitlabIssueTaskParams
        from ..models.create_go_to_meeting_task_params import CreateGoToMeetingTaskParams
        from ..models.create_google_calendar_event_task_params import CreateGoogleCalendarEventTaskParams
        from ..models.create_google_chat_space_task_params import CreateGoogleChatSpaceTaskParams
        from ..models.create_google_docs_page_task_params import CreateGoogleDocsPageTaskParams
        from ..models.create_google_docs_permissions_task_params import CreateGoogleDocsPermissionsTaskParams
        from ..models.create_google_gemini_chat_completion_task_params import CreateGoogleGeminiChatCompletionTaskParams
        from ..models.create_google_meeting_task_params import CreateGoogleMeetingTaskParams
        from ..models.create_incident_postmortem_task_params import CreateIncidentPostmortemTaskParams
        from ..models.create_incident_task_params import CreateIncidentTaskParams
        from ..models.create_jira_issue_task_params import CreateJiraIssueTaskParams
        from ..models.create_jira_subtask_task_params import CreateJiraSubtaskTaskParams
        from ..models.create_jsmops_alert_task_params import CreateJsmopsAlertTaskParams
        from ..models.create_linear_issue_comment_task_params import CreateLinearIssueCommentTaskParams
        from ..models.create_linear_issue_task_params import CreateLinearIssueTaskParams
        from ..models.create_linear_subtask_issue_task_params import CreateLinearSubtaskIssueTaskParams
        from ..models.create_microsoft_teams_channel_task_params import CreateMicrosoftTeamsChannelTaskParams
        from ..models.create_microsoft_teams_chat_task_params import CreateMicrosoftTeamsChatTaskParams
        from ..models.create_microsoft_teams_meeting_task_params import CreateMicrosoftTeamsMeetingTaskParams
        from ..models.create_mistral_chat_completion_task_params import CreateMistralChatCompletionTaskParams
        from ..models.create_motion_task_task_params import CreateMotionTaskTaskParams
        from ..models.create_notion_page_task_params import CreateNotionPageTaskParams
        from ..models.create_openai_chat_completion_task_params import CreateOpenaiChatCompletionTaskParams
        from ..models.create_opsgenie_alert_task_params import CreateOpsgenieAlertTaskParams
        from ..models.create_outlook_event_task_params import CreateOutlookEventTaskParams
        from ..models.create_pagerduty_status_update_task_params import CreatePagerdutyStatusUpdateTaskParams
        from ..models.create_pagertree_alert_task_params import CreatePagertreeAlertTaskParams
        from ..models.create_quip_page_task_params import CreateQuipPageTaskParams
        from ..models.create_service_now_incident_task_params import CreateServiceNowIncidentTaskParams
        from ..models.create_sharepoint_page_task_params import CreateSharepointPageTaskParams
        from ..models.create_shortcut_story_task_params_type_0 import CreateShortcutStoryTaskParamsType0
        from ..models.create_shortcut_story_task_params_type_1 import CreateShortcutStoryTaskParamsType1
        from ..models.create_shortcut_task_task_params import CreateShortcutTaskTaskParams
        from ..models.create_slack_canvas_task_params import CreateSlackCanvasTaskParams
        from ..models.create_slack_channel_task_params import CreateSlackChannelTaskParams
        from ..models.create_sub_incident_task_params import CreateSubIncidentTaskParams
        from ..models.create_trello_card_task_params import CreateTrelloCardTaskParams
        from ..models.create_watsonx_chat_completion_task_params import CreateWatsonxChatCompletionTaskParams
        from ..models.create_webex_meeting_task_params import CreateWebexMeetingTaskParams
        from ..models.create_zendesk_jira_link_task_params import CreateZendeskJiraLinkTaskParams
        from ..models.create_zendesk_ticket_task_params import CreateZendeskTicketTaskParams
        from ..models.create_zoom_meeting_task_params import CreateZoomMeetingTaskParams
        from ..models.get_alerts_task_params import GetAlertsTaskParams
        from ..models.get_github_commits_task_params_type_0 import GetGithubCommitsTaskParamsType0
        from ..models.get_github_commits_task_params_type_1 import GetGithubCommitsTaskParamsType1
        from ..models.get_gitlab_commits_task_params_type_0 import GetGitlabCommitsTaskParamsType0
        from ..models.get_gitlab_commits_task_params_type_1 import GetGitlabCommitsTaskParamsType1
        from ..models.get_pulses_task_params import GetPulsesTaskParams
        from ..models.http_client_task_params import HttpClientTaskParams
        from ..models.invite_to_google_chat_space_task_params import InviteToGoogleChatSpaceTaskParams
        from ..models.invite_to_microsoft_teams_channel_rootly_task_params import (
            InviteToMicrosoftTeamsChannelRootlyTaskParams,
        )
        from ..models.invite_to_microsoft_teams_channel_task_params import InviteToMicrosoftTeamsChannelTaskParams
        from ..models.invite_to_slack_channel_opsgenie_task_params import InviteToSlackChannelOpsgenieTaskParams
        from ..models.invite_to_slack_channel_pagerduty_task_params_type_0 import (
            InviteToSlackChannelPagerdutyTaskParamsType0,
        )
        from ..models.invite_to_slack_channel_pagerduty_task_params_type_1 import (
            InviteToSlackChannelPagerdutyTaskParamsType1,
        )
        from ..models.invite_to_slack_channel_rootly_task_params import InviteToSlackChannelRootlyTaskParams
        from ..models.invite_to_slack_channel_task_params_type_0 import InviteToSlackChannelTaskParamsType0
        from ..models.invite_to_slack_channel_task_params_type_1 import InviteToSlackChannelTaskParamsType1
        from ..models.invite_to_slack_channel_task_params_type_2 import InviteToSlackChannelTaskParamsType2
        from ..models.invite_to_slack_channel_victor_ops_task_params import InviteToSlackChannelVictorOpsTaskParams
        from ..models.page_jsmops_on_call_responders_task_params import PageJsmopsOnCallRespondersTaskParams
        from ..models.page_opsgenie_on_call_responders_task_params import PageOpsgenieOnCallRespondersTaskParams
        from ..models.page_pagerduty_on_call_responders_task_params import PagePagerdutyOnCallRespondersTaskParams
        from ..models.page_rootly_on_call_responders_task_params import PageRootlyOnCallRespondersTaskParams
        from ..models.page_victor_ops_on_call_responders_task_params_type_0 import (
            PageVictorOpsOnCallRespondersTaskParamsType0,
        )
        from ..models.page_victor_ops_on_call_responders_task_params_type_1 import (
            PageVictorOpsOnCallRespondersTaskParamsType1,
        )
        from ..models.print_task_params import PrintTaskParams
        from ..models.publish_incident_task_params import PublishIncidentTaskParams
        from ..models.redis_client_task_params import RedisClientTaskParams
        from ..models.remove_from_slack_channel_task_params import RemoveFromSlackChannelTaskParams
        from ..models.remove_google_docs_permissions_task_params import RemoveGoogleDocsPermissionsTaskParams
        from ..models.rename_google_chat_space_task_params import RenameGoogleChatSpaceTaskParams
        from ..models.rename_microsoft_teams_channel_task_params import RenameMicrosoftTeamsChannelTaskParams
        from ..models.rename_slack_channel_task_params import RenameSlackChannelTaskParams
        from ..models.run_command_heroku_task_params import RunCommandHerokuTaskParams
        from ..models.send_dashboard_report_task_params import SendDashboardReportTaskParams
        from ..models.send_email_task_params import SendEmailTaskParams
        from ..models.send_google_chat_attachments_task_params import SendGoogleChatAttachmentsTaskParams
        from ..models.send_google_chat_message_task_params import SendGoogleChatMessageTaskParams
        from ..models.send_microsoft_teams_blocks_task_params_type_0 import SendMicrosoftTeamsBlocksTaskParamsType0
        from ..models.send_microsoft_teams_chat_message_task_params import SendMicrosoftTeamsChatMessageTaskParams
        from ..models.send_microsoft_teams_message_task_params_type_0 import SendMicrosoftTeamsMessageTaskParamsType0
        from ..models.send_slack_blocks_task_params_type_0 import SendSlackBlocksTaskParamsType0
        from ..models.send_slack_blocks_task_params_type_1 import SendSlackBlocksTaskParamsType1
        from ..models.send_slack_blocks_task_params_type_2 import SendSlackBlocksTaskParamsType2
        from ..models.send_slack_message_task_params_type_0 import SendSlackMessageTaskParamsType0
        from ..models.send_slack_message_task_params_type_1 import SendSlackMessageTaskParamsType1
        from ..models.send_slack_message_task_params_type_2 import SendSlackMessageTaskParamsType2
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
        from ..models.update_coda_page_task_params import UpdateCodaPageTaskParams
        from ..models.update_confluence_page_task_params import UpdateConfluencePageTaskParams
        from ..models.update_datadog_notebook_task_params import UpdateDatadogNotebookTaskParams
        from ..models.update_dropbox_paper_page_task_params import UpdateDropboxPaperPageTaskParams
        from ..models.update_github_issue_task_params import UpdateGithubIssueTaskParams
        from ..models.update_gitlab_issue_task_params import UpdateGitlabIssueTaskParams
        from ..models.update_google_calendar_event_task_params import UpdateGoogleCalendarEventTaskParams
        from ..models.update_google_chat_space_description_task_params import UpdateGoogleChatSpaceDescriptionTaskParams
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
        from ..models.update_quip_page_task_params import UpdateQuipPageTaskParams
        from ..models.update_service_now_incident_task_params import UpdateServiceNowIncidentTaskParams
        from ..models.update_sharepoint_page_task_params import UpdateSharepointPageTaskParams
        from ..models.update_shortcut_story_task_params import UpdateShortcutStoryTaskParams
        from ..models.update_shortcut_task_task_params import UpdateShortcutTaskTaskParams
        from ..models.update_slack_canvas_task_params import UpdateSlackCanvasTaskParams
        from ..models.update_slack_channel_topic_task_params import UpdateSlackChannelTopicTaskParams
        from ..models.update_status_task_params import UpdateStatusTaskParams
        from ..models.update_trello_card_task_params import UpdateTrelloCardTaskParams
        from ..models.update_victor_ops_incident_task_params import UpdateVictorOpsIncidentTaskParams
        from ..models.update_zendesk_ticket_task_params import UpdateZendeskTicketTaskParams

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        position = d.pop("position", UNSET)

        skip_on_failure = d.pop("skip_on_failure", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_task_params(
            data: object,
        ) -> (
            AddActionItemTaskParams
            | AddMicrosoftTeamsChatTabTaskParams
            | AddMicrosoftTeamsTabTaskParamsType0
            | AddMicrosoftTeamsTabTaskParamsType1
            | AddRoleTaskParams
            | AddSlackBookmarkTaskParamsType0
            | AddSlackBookmarkTaskParamsType1
            | AddTeamTaskParams
            | AddToTimelineTaskParams
            | ArchiveGoogleChatSpacesTaskParams
            | ArchiveMicrosoftTeamsChannelsTaskParams
            | ArchiveSlackChannelsTaskParams
            | AttachDatadogDashboardsTaskParams
            | AttachRetrospectivePdfToFreshserviceTicketTaskParams
            | AttachRetrospectivePdfToJiraIssueTaskParams
            | AutoAssignRoleOpsgenieTaskParams
            | AutoAssignRolePagerdutyTaskParamsType0
            | AutoAssignRolePagerdutyTaskParamsType1
            | AutoAssignRoleRootlyTaskParamsType0
            | AutoAssignRoleRootlyTaskParamsType1
            | AutoAssignRoleRootlyTaskParamsType2
            | AutoAssignRoleRootlyTaskParamsType3
            | AutoAssignRoleRootlyTaskParamsType4
            | AutoAssignRoleVictorOpsTaskParams
            | CallPeopleTaskParams
            | ChangeGoogleChatSpacePrivacyTaskParams
            | ChangeSlackChannelPrivacyTaskParams
            | CreateAirtableTableRecordTaskParams
            | CreateAnthropicChatCompletionTaskParams
            | CreateAsanaSubtaskTaskParams
            | CreateAsanaTaskTaskParams
            | CreateClickupTaskTaskParams
            | CreateCodaPageTaskParams
            | CreateConfluencePageTaskParams
            | CreateDatadogNotebookTaskParams
            | CreateDropboxPaperPageTaskParams
            | CreateGithubIssueTaskParams
            | CreateGitlabIssueTaskParams
            | CreateGoogleCalendarEventTaskParams
            | CreateGoogleChatSpaceTaskParams
            | CreateGoogleDocsPageTaskParams
            | CreateGoogleDocsPermissionsTaskParams
            | CreateGoogleGeminiChatCompletionTaskParams
            | CreateGoogleMeetingTaskParams
            | CreateGoToMeetingTaskParams
            | CreateIncidentPostmortemTaskParams
            | CreateIncidentTaskParams
            | CreateJiraIssueTaskParams
            | CreateJiraSubtaskTaskParams
            | CreateJsmopsAlertTaskParams
            | CreateLinearIssueCommentTaskParams
            | CreateLinearIssueTaskParams
            | CreateLinearSubtaskIssueTaskParams
            | CreateMicrosoftTeamsChannelTaskParams
            | CreateMicrosoftTeamsChatTaskParams
            | CreateMicrosoftTeamsMeetingTaskParams
            | CreateMistralChatCompletionTaskParams
            | CreateMotionTaskTaskParams
            | CreateNotionPageTaskParams
            | CreateOpenaiChatCompletionTaskParams
            | CreateOpsgenieAlertTaskParams
            | CreateOutlookEventTaskParams
            | CreatePagerdutyStatusUpdateTaskParams
            | CreatePagertreeAlertTaskParams
            | CreateQuipPageTaskParams
            | CreateServiceNowIncidentTaskParams
            | CreateSharepointPageTaskParams
            | CreateShortcutStoryTaskParamsType0
            | CreateShortcutStoryTaskParamsType1
            | CreateShortcutTaskTaskParams
            | CreateSlackCanvasTaskParams
            | CreateSlackChannelTaskParams
            | CreateSubIncidentTaskParams
            | CreateTrelloCardTaskParams
            | CreateWatsonxChatCompletionTaskParams
            | CreateWebexMeetingTaskParams
            | CreateZendeskJiraLinkTaskParams
            | CreateZendeskTicketTaskParams
            | CreateZoomMeetingTaskParams
            | GetAlertsTaskParams
            | GetGithubCommitsTaskParamsType0
            | GetGithubCommitsTaskParamsType1
            | GetGitlabCommitsTaskParamsType0
            | GetGitlabCommitsTaskParamsType1
            | GetPulsesTaskParams
            | HttpClientTaskParams
            | InviteToGoogleChatSpaceTaskParams
            | InviteToMicrosoftTeamsChannelRootlyTaskParams
            | InviteToMicrosoftTeamsChannelTaskParams
            | InviteToSlackChannelOpsgenieTaskParams
            | InviteToSlackChannelPagerdutyTaskParamsType0
            | InviteToSlackChannelPagerdutyTaskParamsType1
            | InviteToSlackChannelRootlyTaskParams
            | InviteToSlackChannelTaskParamsType0
            | InviteToSlackChannelTaskParamsType1
            | InviteToSlackChannelTaskParamsType2
            | InviteToSlackChannelVictorOpsTaskParams
            | PageJsmopsOnCallRespondersTaskParams
            | PageOpsgenieOnCallRespondersTaskParams
            | PagePagerdutyOnCallRespondersTaskParams
            | PageRootlyOnCallRespondersTaskParams
            | PageVictorOpsOnCallRespondersTaskParamsType0
            | PageVictorOpsOnCallRespondersTaskParamsType1
            | PrintTaskParams
            | PublishIncidentTaskParams
            | RedisClientTaskParams
            | RemoveFromSlackChannelTaskParams
            | RemoveGoogleDocsPermissionsTaskParams
            | RenameGoogleChatSpaceTaskParams
            | RenameMicrosoftTeamsChannelTaskParams
            | RenameSlackChannelTaskParams
            | RunCommandHerokuTaskParams
            | SendDashboardReportTaskParams
            | SendEmailTaskParams
            | SendGoogleChatAttachmentsTaskParams
            | SendGoogleChatMessageTaskParams
            | SendMicrosoftTeamsBlocksTaskParamsType0
            | SendMicrosoftTeamsChatMessageTaskParams
            | SendMicrosoftTeamsMessageTaskParamsType0
            | SendSlackBlocksTaskParamsType0
            | SendSlackBlocksTaskParamsType1
            | SendSlackBlocksTaskParamsType2
            | SendSlackMessageTaskParamsType0
            | SendSlackMessageTaskParamsType1
            | SendSlackMessageTaskParamsType2
            | SendSmsTaskParams
            | SendWhatsappMessageTaskParams
            | SnapshotDatadogGraphTaskParams
            | SnapshotGrafanaDashboardTaskParams
            | SnapshotLookerLookTaskParams
            | SnapshotNewRelicGraphTaskParams
            | TriggerWorkflowTaskParams
            | TweetTwitterMessageTaskParams
            | Unset
            | UpdateActionItemTaskParams
            | UpdateAirtableTableRecordTaskParams
            | UpdateAsanaTaskTaskParams
            | UpdateAttachedAlertsTaskParams
            | UpdateClickupTaskTaskParams
            | UpdateCodaPageTaskParams
            | UpdateConfluencePageTaskParams
            | UpdateDatadogNotebookTaskParams
            | UpdateDropboxPaperPageTaskParams
            | UpdateGithubIssueTaskParams
            | UpdateGitlabIssueTaskParams
            | UpdateGoogleCalendarEventTaskParams
            | UpdateGoogleChatSpaceDescriptionTaskParams
            | UpdateGoogleDocsPageTaskParams
            | UpdateIncidentPostmortemTaskParams
            | UpdateIncidentStatusTimestampTaskParams
            | UpdateIncidentTaskParams
            | UpdateJiraIssueTaskParams
            | UpdateLinearIssueTaskParams
            | UpdateMotionTaskTaskParams
            | UpdateNotionPageTaskParams
            | UpdateOpsgenieAlertTaskParams
            | UpdateOpsgenieIncidentTaskParams
            | UpdatePagerdutyIncidentTaskParams
            | UpdatePagertreeAlertTaskParams
            | UpdateQuipPageTaskParams
            | UpdateServiceNowIncidentTaskParams
            | UpdateSharepointPageTaskParams
            | UpdateShortcutStoryTaskParams
            | UpdateShortcutTaskTaskParams
            | UpdateSlackCanvasTaskParams
            | UpdateSlackChannelTopicTaskParams
            | UpdateStatusTaskParams
            | UpdateTrelloCardTaskParams
            | UpdateVictorOpsIncidentTaskParams
            | UpdateZendeskTicketTaskParams
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_0 = AddActionItemTaskParams.from_dict(data)

                return task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_1 = UpdateActionItemTaskParams.from_dict(data)

                return task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_2 = AddRoleTaskParams.from_dict(data)

                return task_params_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasadd_slack_bookmark_task_params_type_0 = AddSlackBookmarkTaskParamsType0.from_dict(data)

                return componentsschemasadd_slack_bookmark_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasadd_slack_bookmark_task_params_type_1 = AddSlackBookmarkTaskParamsType1.from_dict(data)

                return componentsschemasadd_slack_bookmark_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_4 = AddTeamTaskParams.from_dict(data)

                return task_params_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_5 = AddToTimelineTaskParams.from_dict(data)

                return task_params_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_6 = ArchiveSlackChannelsTaskParams.from_dict(data)

                return task_params_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_7 = AttachDatadogDashboardsTaskParams.from_dict(data)

                return task_params_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_8 = AutoAssignRoleOpsgenieTaskParams.from_dict(data)

                return task_params_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasauto_assign_role_rootly_task_params_type_0 = (
                    AutoAssignRoleRootlyTaskParamsType0.from_dict(data)
                )

                return componentsschemasauto_assign_role_rootly_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasauto_assign_role_rootly_task_params_type_1 = (
                    AutoAssignRoleRootlyTaskParamsType1.from_dict(data)
                )

                return componentsschemasauto_assign_role_rootly_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasauto_assign_role_rootly_task_params_type_2 = (
                    AutoAssignRoleRootlyTaskParamsType2.from_dict(data)
                )

                return componentsschemasauto_assign_role_rootly_task_params_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasauto_assign_role_rootly_task_params_type_3 = (
                    AutoAssignRoleRootlyTaskParamsType3.from_dict(data)
                )

                return componentsschemasauto_assign_role_rootly_task_params_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasauto_assign_role_rootly_task_params_type_4 = (
                    AutoAssignRoleRootlyTaskParamsType4.from_dict(data)
                )

                return componentsschemasauto_assign_role_rootly_task_params_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasauto_assign_role_pagerduty_task_params_type_0 = (
                    AutoAssignRolePagerdutyTaskParamsType0.from_dict(data)
                )

                return componentsschemasauto_assign_role_pagerduty_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasauto_assign_role_pagerduty_task_params_type_1 = (
                    AutoAssignRolePagerdutyTaskParamsType1.from_dict(data)
                )

                return componentsschemasauto_assign_role_pagerduty_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_11 = UpdatePagerdutyIncidentTaskParams.from_dict(data)

                return task_params_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_12 = CreatePagerdutyStatusUpdateTaskParams.from_dict(data)

                return task_params_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_13 = CreatePagertreeAlertTaskParams.from_dict(data)

                return task_params_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_14 = UpdatePagertreeAlertTaskParams.from_dict(data)

                return task_params_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_15 = AutoAssignRoleVictorOpsTaskParams.from_dict(data)

                return task_params_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_16 = CallPeopleTaskParams.from_dict(data)

                return task_params_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_17 = CreateAirtableTableRecordTaskParams.from_dict(data)

                return task_params_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_18 = CreateAsanaSubtaskTaskParams.from_dict(data)

                return task_params_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_19 = CreateAsanaTaskTaskParams.from_dict(data)

                return task_params_type_19
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_20 = CreateConfluencePageTaskParams.from_dict(data)

                return task_params_type_20
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_21 = CreateDatadogNotebookTaskParams.from_dict(data)

                return task_params_type_21
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_22 = CreateCodaPageTaskParams.from_dict(data)

                return task_params_type_22
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_23 = CreateDropboxPaperPageTaskParams.from_dict(data)

                return task_params_type_23
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_24 = CreateGithubIssueTaskParams.from_dict(data)

                return task_params_type_24
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_25 = CreateGitlabIssueTaskParams.from_dict(data)

                return task_params_type_25
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_26 = CreateOutlookEventTaskParams.from_dict(data)

                return task_params_type_26
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_27 = CreateGoogleCalendarEventTaskParams.from_dict(data)

                return task_params_type_27
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_28 = UpdateGoogleDocsPageTaskParams.from_dict(data)

                return task_params_type_28
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_29 = UpdateCodaPageTaskParams.from_dict(data)

                return task_params_type_29
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_30 = UpdateGoogleCalendarEventTaskParams.from_dict(data)

                return task_params_type_30
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_31 = CreateSharepointPageTaskParams.from_dict(data)

                return task_params_type_31
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_32 = CreateGoogleDocsPageTaskParams.from_dict(data)

                return task_params_type_32
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_33 = CreateGoogleDocsPermissionsTaskParams.from_dict(data)

                return task_params_type_33
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_34 = RemoveGoogleDocsPermissionsTaskParams.from_dict(data)

                return task_params_type_34
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_35 = CreateQuipPageTaskParams.from_dict(data)

                return task_params_type_35
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_36 = CreateGoogleMeetingTaskParams.from_dict(data)

                return task_params_type_36
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_37 = CreateGoToMeetingTaskParams.from_dict(data)

                return task_params_type_37
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_38 = CreateIncidentTaskParams.from_dict(data)

                return task_params_type_38
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_39 = CreateSubIncidentTaskParams.from_dict(data)

                return task_params_type_39
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_40 = CreateIncidentPostmortemTaskParams.from_dict(data)

                return task_params_type_40
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_41 = CreateJiraIssueTaskParams.from_dict(data)

                return task_params_type_41
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_42 = CreateJiraSubtaskTaskParams.from_dict(data)

                return task_params_type_42
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_43 = AttachRetrospectivePdfToJiraIssueTaskParams.from_dict(data)

                return task_params_type_43
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_44 = AttachRetrospectivePdfToFreshserviceTicketTaskParams.from_dict(data)

                return task_params_type_44
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_45 = CreateLinearIssueTaskParams.from_dict(data)

                return task_params_type_45
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_46 = CreateLinearSubtaskIssueTaskParams.from_dict(data)

                return task_params_type_46
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_47 = CreateLinearIssueCommentTaskParams.from_dict(data)

                return task_params_type_47
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_48 = CreateMicrosoftTeamsMeetingTaskParams.from_dict(data)

                return task_params_type_48
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_49 = CreateMicrosoftTeamsChannelTaskParams.from_dict(data)

                return task_params_type_49
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_50 = CreateMicrosoftTeamsChatTaskParams.from_dict(data)

                return task_params_type_50
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasadd_microsoft_teams_tab_task_params_type_0 = (
                    AddMicrosoftTeamsTabTaskParamsType0.from_dict(data)
                )

                return componentsschemasadd_microsoft_teams_tab_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasadd_microsoft_teams_tab_task_params_type_1 = (
                    AddMicrosoftTeamsTabTaskParamsType1.from_dict(data)
                )

                return componentsschemasadd_microsoft_teams_tab_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_52 = AddMicrosoftTeamsChatTabTaskParams.from_dict(data)

                return task_params_type_52
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_53 = CreateGoogleChatSpaceTaskParams.from_dict(data)

                return task_params_type_53
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_54 = SendGoogleChatMessageTaskParams.from_dict(data)

                return task_params_type_54
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_55 = SendGoogleChatAttachmentsTaskParams.from_dict(data)

                return task_params_type_55
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_56 = InviteToGoogleChatSpaceTaskParams.from_dict(data)

                return task_params_type_56
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_57 = ArchiveGoogleChatSpacesTaskParams.from_dict(data)

                return task_params_type_57
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_58 = RenameGoogleChatSpaceTaskParams.from_dict(data)

                return task_params_type_58
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_59 = UpdateGoogleChatSpaceDescriptionTaskParams.from_dict(data)

                return task_params_type_59
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_60 = ChangeGoogleChatSpacePrivacyTaskParams.from_dict(data)

                return task_params_type_60
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_61 = ArchiveMicrosoftTeamsChannelsTaskParams.from_dict(data)

                return task_params_type_61
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_62 = RenameMicrosoftTeamsChannelTaskParams.from_dict(data)

                return task_params_type_62
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_63 = InviteToMicrosoftTeamsChannelTaskParams.from_dict(data)

                return task_params_type_63
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_64 = CreateNotionPageTaskParams.from_dict(data)

                return task_params_type_64
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_microsoft_teams_message_task_params_type_0 = (
                    SendMicrosoftTeamsMessageTaskParamsType0.from_dict(data)
                )

                return componentsschemassend_microsoft_teams_message_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_66 = SendMicrosoftTeamsChatMessageTaskParams.from_dict(data)

                return task_params_type_66
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_microsoft_teams_blocks_task_params_type_0 = (
                    SendMicrosoftTeamsBlocksTaskParamsType0.from_dict(data)
                )

                return componentsschemassend_microsoft_teams_blocks_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_68 = UpdateNotionPageTaskParams.from_dict(data)

                return task_params_type_68
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_69 = UpdateQuipPageTaskParams.from_dict(data)

                return task_params_type_69
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_70 = UpdateConfluencePageTaskParams.from_dict(data)

                return task_params_type_70
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_71 = UpdateSharepointPageTaskParams.from_dict(data)

                return task_params_type_71
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_72 = UpdateDropboxPaperPageTaskParams.from_dict(data)

                return task_params_type_72
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_73 = UpdateDatadogNotebookTaskParams.from_dict(data)

                return task_params_type_73
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_74 = CreateServiceNowIncidentTaskParams.from_dict(data)

                return task_params_type_74
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascreate_shortcut_story_task_params_type_0 = (
                    CreateShortcutStoryTaskParamsType0.from_dict(data)
                )

                return componentsschemascreate_shortcut_story_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascreate_shortcut_story_task_params_type_1 = (
                    CreateShortcutStoryTaskParamsType1.from_dict(data)
                )

                return componentsschemascreate_shortcut_story_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_76 = CreateShortcutTaskTaskParams.from_dict(data)

                return task_params_type_76
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_77 = CreateTrelloCardTaskParams.from_dict(data)

                return task_params_type_77
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_78 = CreateWebexMeetingTaskParams.from_dict(data)

                return task_params_type_78
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_79 = CreateZendeskTicketTaskParams.from_dict(data)

                return task_params_type_79
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_80 = CreateZendeskJiraLinkTaskParams.from_dict(data)

                return task_params_type_80
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_81 = CreateClickupTaskTaskParams.from_dict(data)

                return task_params_type_81
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_82 = CreateMotionTaskTaskParams.from_dict(data)

                return task_params_type_82
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_83 = CreateZoomMeetingTaskParams.from_dict(data)

                return task_params_type_83
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasget_github_commits_task_params_type_0 = GetGithubCommitsTaskParamsType0.from_dict(data)

                return componentsschemasget_github_commits_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasget_github_commits_task_params_type_1 = GetGithubCommitsTaskParamsType1.from_dict(data)

                return componentsschemasget_github_commits_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasget_gitlab_commits_task_params_type_0 = GetGitlabCommitsTaskParamsType0.from_dict(data)

                return componentsschemasget_gitlab_commits_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasget_gitlab_commits_task_params_type_1 = GetGitlabCommitsTaskParamsType1.from_dict(data)

                return componentsschemasget_gitlab_commits_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_86 = GetPulsesTaskParams.from_dict(data)

                return task_params_type_86
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_87 = GetAlertsTaskParams.from_dict(data)

                return task_params_type_87
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_88 = HttpClientTaskParams.from_dict(data)

                return task_params_type_88
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_89 = InviteToSlackChannelOpsgenieTaskParams.from_dict(data)

                return task_params_type_89
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_90 = InviteToSlackChannelRootlyTaskParams.from_dict(data)

                return task_params_type_90
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_91 = InviteToMicrosoftTeamsChannelRootlyTaskParams.from_dict(data)

                return task_params_type_91
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasinvite_to_slack_channel_pagerduty_task_params_type_0 = (
                    InviteToSlackChannelPagerdutyTaskParamsType0.from_dict(data)
                )

                return componentsschemasinvite_to_slack_channel_pagerduty_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasinvite_to_slack_channel_pagerduty_task_params_type_1 = (
                    InviteToSlackChannelPagerdutyTaskParamsType1.from_dict(data)
                )

                return componentsschemasinvite_to_slack_channel_pagerduty_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasinvite_to_slack_channel_task_params_type_0 = (
                    InviteToSlackChannelTaskParamsType0.from_dict(data)
                )

                return componentsschemasinvite_to_slack_channel_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasinvite_to_slack_channel_task_params_type_1 = (
                    InviteToSlackChannelTaskParamsType1.from_dict(data)
                )

                return componentsschemasinvite_to_slack_channel_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasinvite_to_slack_channel_task_params_type_2 = (
                    InviteToSlackChannelTaskParamsType2.from_dict(data)
                )

                return componentsschemasinvite_to_slack_channel_task_params_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_94 = InviteToSlackChannelVictorOpsTaskParams.from_dict(data)

                return task_params_type_94
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_95 = PageOpsgenieOnCallRespondersTaskParams.from_dict(data)

                return task_params_type_95
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_96 = CreateOpsgenieAlertTaskParams.from_dict(data)

                return task_params_type_96
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_97 = CreateJsmopsAlertTaskParams.from_dict(data)

                return task_params_type_97
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_98 = PageJsmopsOnCallRespondersTaskParams.from_dict(data)

                return task_params_type_98
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_99 = UpdateOpsgenieAlertTaskParams.from_dict(data)

                return task_params_type_99
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_100 = UpdateOpsgenieIncidentTaskParams.from_dict(data)

                return task_params_type_100
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_101 = PageRootlyOnCallRespondersTaskParams.from_dict(data)

                return task_params_type_101
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_102 = PagePagerdutyOnCallRespondersTaskParams.from_dict(data)

                return task_params_type_102
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemaspage_victor_ops_on_call_responders_task_params_type_0 = (
                    PageVictorOpsOnCallRespondersTaskParamsType0.from_dict(data)
                )

                return componentsschemaspage_victor_ops_on_call_responders_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemaspage_victor_ops_on_call_responders_task_params_type_1 = (
                    PageVictorOpsOnCallRespondersTaskParamsType1.from_dict(data)
                )

                return componentsschemaspage_victor_ops_on_call_responders_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_104 = UpdateVictorOpsIncidentTaskParams.from_dict(data)

                return task_params_type_104
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_105 = PrintTaskParams.from_dict(data)

                return task_params_type_105
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_106 = PublishIncidentTaskParams.from_dict(data)

                return task_params_type_106
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_107 = RedisClientTaskParams.from_dict(data)

                return task_params_type_107
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_108 = RenameSlackChannelTaskParams.from_dict(data)

                return task_params_type_108
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_109 = RemoveFromSlackChannelTaskParams.from_dict(data)

                return task_params_type_109
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_110 = ChangeSlackChannelPrivacyTaskParams.from_dict(data)

                return task_params_type_110
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_111 = RunCommandHerokuTaskParams.from_dict(data)

                return task_params_type_111
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_112 = SendEmailTaskParams.from_dict(data)

                return task_params_type_112
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_113 = SendDashboardReportTaskParams.from_dict(data)

                return task_params_type_113
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_114 = CreateSlackChannelTaskParams.from_dict(data)

                return task_params_type_114
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_115 = CreateSlackCanvasTaskParams.from_dict(data)

                return task_params_type_115
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_slack_message_task_params_type_0 = SendSlackMessageTaskParamsType0.from_dict(data)

                return componentsschemassend_slack_message_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_slack_message_task_params_type_1 = SendSlackMessageTaskParamsType1.from_dict(data)

                return componentsschemassend_slack_message_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_slack_message_task_params_type_2 = SendSlackMessageTaskParamsType2.from_dict(data)

                return componentsschemassend_slack_message_task_params_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_117 = SendSmsTaskParams.from_dict(data)

                return task_params_type_117
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_118 = SendWhatsappMessageTaskParams.from_dict(data)

                return task_params_type_118
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_119 = SnapshotDatadogGraphTaskParams.from_dict(data)

                return task_params_type_119
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_120 = SnapshotGrafanaDashboardTaskParams.from_dict(data)

                return task_params_type_120
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_121 = SnapshotLookerLookTaskParams.from_dict(data)

                return task_params_type_121
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_122 = SnapshotNewRelicGraphTaskParams.from_dict(data)

                return task_params_type_122
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_123 = TweetTwitterMessageTaskParams.from_dict(data)

                return task_params_type_123
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_124 = UpdateAirtableTableRecordTaskParams.from_dict(data)

                return task_params_type_124
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_125 = UpdateAsanaTaskTaskParams.from_dict(data)

                return task_params_type_125
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_126 = UpdateGithubIssueTaskParams.from_dict(data)

                return task_params_type_126
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_127 = UpdateGitlabIssueTaskParams.from_dict(data)

                return task_params_type_127
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_128 = UpdateIncidentTaskParams.from_dict(data)

                return task_params_type_128
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_129 = UpdateIncidentPostmortemTaskParams.from_dict(data)

                return task_params_type_129
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_130 = UpdateJiraIssueTaskParams.from_dict(data)

                return task_params_type_130
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_131 = UpdateLinearIssueTaskParams.from_dict(data)

                return task_params_type_131
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_132 = UpdateServiceNowIncidentTaskParams.from_dict(data)

                return task_params_type_132
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_133 = UpdateShortcutStoryTaskParams.from_dict(data)

                return task_params_type_133
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_134 = UpdateShortcutTaskTaskParams.from_dict(data)

                return task_params_type_134
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_135 = UpdateSlackChannelTopicTaskParams.from_dict(data)

                return task_params_type_135
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_136 = UpdateSlackCanvasTaskParams.from_dict(data)

                return task_params_type_136
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_137 = UpdateStatusTaskParams.from_dict(data)

                return task_params_type_137
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_138 = UpdateIncidentStatusTimestampTaskParams.from_dict(data)

                return task_params_type_138
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_139 = UpdateTrelloCardTaskParams.from_dict(data)

                return task_params_type_139
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_140 = UpdateClickupTaskTaskParams.from_dict(data)

                return task_params_type_140
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_141 = UpdateMotionTaskTaskParams.from_dict(data)

                return task_params_type_141
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_142 = UpdateZendeskTicketTaskParams.from_dict(data)

                return task_params_type_142
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_143 = UpdateAttachedAlertsTaskParams.from_dict(data)

                return task_params_type_143
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_144 = TriggerWorkflowTaskParams.from_dict(data)

                return task_params_type_144
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_slack_blocks_task_params_type_0 = SendSlackBlocksTaskParamsType0.from_dict(data)

                return componentsschemassend_slack_blocks_task_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_slack_blocks_task_params_type_1 = SendSlackBlocksTaskParamsType1.from_dict(data)

                return componentsschemassend_slack_blocks_task_params_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemassend_slack_blocks_task_params_type_2 = SendSlackBlocksTaskParamsType2.from_dict(data)

                return componentsschemassend_slack_blocks_task_params_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_146 = CreateOpenaiChatCompletionTaskParams.from_dict(data)

                return task_params_type_146
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_147 = CreateWatsonxChatCompletionTaskParams.from_dict(data)

                return task_params_type_147
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_148 = CreateGoogleGeminiChatCompletionTaskParams.from_dict(data)

                return task_params_type_148
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_params_type_149 = CreateMistralChatCompletionTaskParams.from_dict(data)

                return task_params_type_149
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            task_params_type_150 = CreateAnthropicChatCompletionTaskParams.from_dict(data)

            return task_params_type_150

        task_params = _parse_task_params(d.pop("task_params", UNSET))

        update_workflow_task_data_attributes = cls(
            name=name,
            position=position,
            skip_on_failure=skip_on_failure,
            enabled=enabled,
            task_params=task_params,
        )

        return update_workflow_task_data_attributes
