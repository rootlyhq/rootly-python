from typing import Literal, cast

CreateDatadogNotebookTaskParamsTaskType = Literal["create_datadog_notebook"]

CREATE_DATADOG_NOTEBOOK_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateDatadogNotebookTaskParamsTaskType] = {
    "create_datadog_notebook",
}


def check_create_datadog_notebook_task_params_task_type(value: str | None) -> CreateDatadogNotebookTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_DATADOG_NOTEBOOK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateDatadogNotebookTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_DATADOG_NOTEBOOK_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
