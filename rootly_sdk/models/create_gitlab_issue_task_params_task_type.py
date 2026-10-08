from typing import Literal

CreateGitlabIssueTaskParamsTaskType = Literal["create_gitlab_issue"]

CREATE_GITLAB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGitlabIssueTaskParamsTaskType] = {
    "create_gitlab_issue",
}


def check_create_gitlab_issue_task_params_task_type(value: str | None) -> CreateGitlabIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GITLAB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_GITLAB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
