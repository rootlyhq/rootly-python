from typing import Literal, cast

UpdateActionItemTaskParamsAttributeToQueryBy = Literal[
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
    "shortcut_story_id",
    "shortcut_task_id",
    "trello_card_id",
    "zendesk_ticket_id",
]

UPDATE_ACTION_ITEM_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES: set[UpdateActionItemTaskParamsAttributeToQueryBy] = {
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
    "shortcut_story_id",
    "shortcut_task_id",
    "trello_card_id",
    "zendesk_ticket_id",
}


def check_update_action_item_task_params_attribute_to_query_by(
    value: str | None,
) -> UpdateActionItemTaskParamsAttributeToQueryBy | None:
    if value is None:
        return None
    if value in UPDATE_ACTION_ITEM_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES:
        return cast(UpdateActionItemTaskParamsAttributeToQueryBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ACTION_ITEM_TASK_PARAMS_ATTRIBUTE_TO_QUERY_BY_VALUES!r}"
    )
