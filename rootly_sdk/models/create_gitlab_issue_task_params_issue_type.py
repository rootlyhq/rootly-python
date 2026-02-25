from typing import Literal, cast

CreateGitlabIssueTaskParamsIssueType = Literal["incident", "issue", "task", "test_case"]

CREATE_GITLAB_ISSUE_TASK_PARAMS_ISSUE_TYPE_VALUES: set[CreateGitlabIssueTaskParamsIssueType] = {
    "incident",
    "issue",
    "task",
    "test_case",
}


def check_create_gitlab_issue_task_params_issue_type(value: str | None) -> CreateGitlabIssueTaskParamsIssueType | None:
    if value is None:
        return None
    if value in CREATE_GITLAB_ISSUE_TASK_PARAMS_ISSUE_TYPE_VALUES:
        return cast(CreateGitlabIssueTaskParamsIssueType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GITLAB_ISSUE_TASK_PARAMS_ISSUE_TYPE_VALUES!r}"
    )
