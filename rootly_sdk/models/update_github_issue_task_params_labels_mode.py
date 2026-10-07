from typing import Literal

UpdateGithubIssueTaskParamsLabelsMode = Literal["append", "replace"]

UPDATE_GITHUB_ISSUE_TASK_PARAMS_LABELS_MODE_VALUES: set[UpdateGithubIssueTaskParamsLabelsMode] = {
    "append",
    "replace",
}


def check_update_github_issue_task_params_labels_mode(
    value: str | None,
) -> UpdateGithubIssueTaskParamsLabelsMode | None:
    if value is None:
        return None
    if value in UPDATE_GITHUB_ISSUE_TASK_PARAMS_LABELS_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_GITHUB_ISSUE_TASK_PARAMS_LABELS_MODE_VALUES!r}"
    )
