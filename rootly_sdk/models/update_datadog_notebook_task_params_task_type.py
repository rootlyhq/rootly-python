from typing import Literal, cast

UpdateDatadogNotebookTaskParamsTaskType = Literal["update_datadog_notebook"]

UPDATE_DATADOG_NOTEBOOK_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateDatadogNotebookTaskParamsTaskType] = {
    "update_datadog_notebook",
}


def check_update_datadog_notebook_task_params_task_type(
    value: str | None,
) -> UpdateDatadogNotebookTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_DATADOG_NOTEBOOK_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateDatadogNotebookTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DATADOG_NOTEBOOK_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
