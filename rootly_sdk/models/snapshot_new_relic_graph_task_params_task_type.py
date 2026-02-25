from typing import Literal, cast

SnapshotNewRelicGraphTaskParamsTaskType = Literal["snapshot_looker_graph"]

SNAPSHOT_NEW_RELIC_GRAPH_TASK_PARAMS_TASK_TYPE_VALUES: set[SnapshotNewRelicGraphTaskParamsTaskType] = {
    "snapshot_looker_graph",
}


def check_snapshot_new_relic_graph_task_params_task_type(
    value: str | None,
) -> SnapshotNewRelicGraphTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SNAPSHOT_NEW_RELIC_GRAPH_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SnapshotNewRelicGraphTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SNAPSHOT_NEW_RELIC_GRAPH_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
