from typing import Literal, cast

SnapshotDatadogGraphTaskParamsTaskType = Literal["snapshot_datadog_graph"]

SNAPSHOT_DATADOG_GRAPH_TASK_PARAMS_TASK_TYPE_VALUES: set[SnapshotDatadogGraphTaskParamsTaskType] = {
    "snapshot_datadog_graph",
}


def check_snapshot_datadog_graph_task_params_task_type(
    value: str | None,
) -> SnapshotDatadogGraphTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SNAPSHOT_DATADOG_GRAPH_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SnapshotDatadogGraphTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SNAPSHOT_DATADOG_GRAPH_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
