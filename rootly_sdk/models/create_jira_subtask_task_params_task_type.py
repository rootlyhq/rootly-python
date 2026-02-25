from typing import Literal, cast

CreateJiraSubtaskTaskParamsTaskType = Literal["create_jira_subtask"]

CREATE_JIRA_SUBTASK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateJiraSubtaskTaskParamsTaskType] = {
    "create_jira_subtask",
}


def check_create_jira_subtask_task_params_task_type(value: str | None) -> CreateJiraSubtaskTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_JIRA_SUBTASK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateJiraSubtaskTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_JIRA_SUBTASK_TASK_PARAMS_TASK_TYPE_VALUES!r}")
