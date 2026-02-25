from typing import Literal, cast

UpdateLinearIssueTaskParamsTaskType = Literal["update_linear_issue"]

UPDATE_LINEAR_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateLinearIssueTaskParamsTaskType] = {
    "update_linear_issue",
}


def check_update_linear_issue_task_params_task_type(value: str | None) -> UpdateLinearIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_LINEAR_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateLinearIssueTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_LINEAR_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
