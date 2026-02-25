from typing import Literal, cast

CreateLinearSubtaskIssueTaskParamsTaskType = Literal["create_linear_subtask_issue"]

CREATE_LINEAR_SUBTASK_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateLinearSubtaskIssueTaskParamsTaskType] = {
    "create_linear_subtask_issue",
}


def check_create_linear_subtask_issue_task_params_task_type(value: str | None) -> CreateLinearSubtaskIssueTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_LINEAR_SUBTASK_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateLinearSubtaskIssueTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_LINEAR_SUBTASK_ISSUE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
