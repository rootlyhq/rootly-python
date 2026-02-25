from typing import Literal, cast

UpdateGitlabIssueTaskParamsTaskType = Literal["update_gitlab_issue"]

UPDATE_GITLAB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateGitlabIssueTaskParamsTaskType] = {
    "update_gitlab_issue",
}


def check_update_gitlab_issue_task_params_task_type(value: str | None) -> UpdateGitlabIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_GITLAB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateGitlabIssueTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_GITLAB_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
