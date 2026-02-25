from typing import Literal, cast

UpdateJiraIssueTaskParamsTaskType = Literal["update_jira_issue"]

UPDATE_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateJiraIssueTaskParamsTaskType] = {
    "update_jira_issue",
}


def check_update_jira_issue_task_params_task_type(value: str | None) -> UpdateJiraIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateJiraIssueTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
