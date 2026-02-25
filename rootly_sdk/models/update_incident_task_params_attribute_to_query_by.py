from typing import Literal, cast

UpdateIncidentTaskParamsAttributeToQueryBy = Literal[
    "airtable_record_id",
    "asana_task_id",
    "clickup_task_id",
    "freshservice_task_id",
    "freshservice_ticket_id",
    "github_issue_id",
    "gitlab_issue_id",
    "id",
    "jira_issue_id",
    "linear_issue_id",
    "motion_task_id",
    "opsgenie_incident_id",
    "pagerduty_incident_id",
    "sequential_id",
    "shortcut_story_id",
    "shortcut_task_id",
    "slug",
    "trello_card_id",
    "victor_ops_incident_id",
    "zendesk_ticket_id",
]

UPDATE_INCIDENT_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES: set[UpdateIncidentTaskParamsAttributeToQueryBy] = {
    "airtable_record_id",
    "asana_task_id",
    "clickup_task_id",
    "freshservice_task_id",
    "freshservice_ticket_id",
    "github_issue_id",
    "gitlab_issue_id",
    "id",
    "jira_issue_id",
    "linear_issue_id",
    "motion_task_id",
    "opsgenie_incident_id",
    "pagerduty_incident_id",
    "sequential_id",
    "shortcut_story_id",
    "shortcut_task_id",
    "slug",
    "trello_card_id",
    "victor_ops_incident_id",
    "zendesk_ticket_id",
}


def check_update_incident_task_params_attribute_to_query_by(value: str | None) -> UpdateIncidentTaskParamsAttributeToQueryBy | None:
    if value is None:
        return None
    if value in UPDATE_INCIDENT_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES:
        return cast(UpdateIncidentTaskParamsAttributeToQueryBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INCIDENT_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES!r}"
    )
