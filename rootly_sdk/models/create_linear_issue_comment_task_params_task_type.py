from typing import Literal, cast

CreateLinearIssueCommentTaskParamsTaskType = Literal["create_linear_issue_comment"]

CREATE_LINEAR_ISSUE_COMMENT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateLinearIssueCommentTaskParamsTaskType] = {
    "create_linear_issue_comment",
}


def check_create_linear_issue_comment_task_params_task_type(
    value: str | None,
) -> CreateLinearIssueCommentTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_LINEAR_ISSUE_COMMENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateLinearIssueCommentTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_LINEAR_ISSUE_COMMENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
