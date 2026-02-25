from typing import Literal, cast

CreateGithubIssueTaskParamsTaskType = Literal["create_github_issue"]

CREATE_GITHUB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGithubIssueTaskParamsTaskType] = {
    "create_github_issue",
}


def check_create_github_issue_task_params_task_type(value: str | None) -> CreateGithubIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GITHUB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGithubIssueTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_GITHUB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
