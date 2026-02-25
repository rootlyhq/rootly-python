from typing import Literal, cast

CreateJiraIssueTaskParamsTaskType = Literal["create_jira_issue"]

CREATE_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateJiraIssueTaskParamsTaskType] = {
    "create_jira_issue",
}


def check_create_jira_issue_task_params_task_type(value: str | None) -> CreateJiraIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateJiraIssueTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_JIRA_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
