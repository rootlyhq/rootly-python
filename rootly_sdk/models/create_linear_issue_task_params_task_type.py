from typing import Literal, cast

CreateLinearIssueTaskParamsTaskType = Literal["create_linear_issue"]

CREATE_LINEAR_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateLinearIssueTaskParamsTaskType] = {
    "create_linear_issue",
}


def check_create_linear_issue_task_params_task_type(value: str | None) -> CreateLinearIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_LINEAR_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateLinearIssueTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_LINEAR_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
