from typing import Literal, cast

CreateDatadogNotebookTaskParamsKind = Literal["documentation", "investigation", "postmortem", "report", "runbook"]

CREATE_DATADOG_NOTEBOOK_TASK_PARAMS_KIND_VALUES: set[CreateDatadogNotebookTaskParamsKind] = {
    "documentation",
    "investigation",
    "postmortem",
    "report",
    "runbook",
}


def check_create_datadog_notebook_task_params_kind(value: str | None) -> CreateDatadogNotebookTaskParamsKind | None:
    if value is None:
        return None
    if value in CREATE_DATADOG_NOTEBOOK_TASK_PARAMS_KIND_VALUES:
        return cast(CreateDatadogNotebookTaskParamsKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_DATADOG_NOTEBOOK_TASK_PARAMS_KIND_VALUES!r}")
