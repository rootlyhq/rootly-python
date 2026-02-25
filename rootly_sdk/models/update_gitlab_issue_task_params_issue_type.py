from typing import Literal, cast

UpdateGitlabIssueTaskParamsIssueType = Literal["incident", "issue", "task", "test_case"]

UPDATE_GITLAB_ISSUE_TASK_PARAMS_ISSUE_TYPE_VALUES: set[UpdateGitlabIssueTaskParamsIssueType] = {
    "incident",
    "issue",
    "task",
    "test_case",
}


def check_update_gitlab_issue_task_params_issue_type(value: str | None) -> UpdateGitlabIssueTaskParamsIssueType | None:
    if value is None:
        return None
    if value in UPDATE_GITLAB_ISSUE_TASK_PARAMS_ISSUE_TYPE_VALUES:
        return cast(UpdateGitlabIssueTaskParamsIssueType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_GITLAB_ISSUE_TASK_PARAMS_ISSUE_TYPE_VALUES!r}"
    )
