from typing import Literal, cast

UpdateGithubIssueTaskParamsTaskType = Literal["update_github_issue"]

UPDATE_GITHUB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateGithubIssueTaskParamsTaskType] = {
    "update_github_issue",
}


def check_update_github_issue_task_params_task_type(value: str | None) -> UpdateGithubIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_GITHUB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateGithubIssueTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_GITHUB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
