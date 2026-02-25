from typing import Literal, cast

UpdateDatadogNotebookTaskParamsKind = Literal["documentation", "investigation", "postmortem", "report", "runbook"]

UPDATE_DATADOG_NOTEBOOK_TASK_PARAMS_KIND_VALUES: set[UpdateDatadogNotebookTaskParamsKind] = {
    "documentation",
    "investigation",
    "postmortem",
    "report",
    "runbook",
}


def check_update_datadog_notebook_task_params_kind(value: str | None) -> UpdateDatadogNotebookTaskParamsKind | None:
    if value is None:
        return None
    if value in UPDATE_DATADOG_NOTEBOOK_TASK_PARAMS_KIND_VALUES:
        return cast(UpdateDatadogNotebookTaskParamsKind, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_DATADOG_NOTEBOOK_TASK_PARAMS_KIND_VALUES!r}")
