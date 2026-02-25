from typing import Literal, cast

SnapshotNewRelicGraphTaskParamsMetricType = Literal[
    "APDEX",
    "AREA",
    "BAR",
    "BASELINE",
    "BILLBOARD",
    "BULLET",
    "EVENT_FEED",
    "FUNNEL",
    "HEATMAP",
    "HISTOGRAM",
    "LINE",
    "PIE",
    "SCATTER",
    "STACKED_HORIZONTAL_BAR",
    "TABLE",
    "VERTICAL_BAR",
]

SNAPSHOT_NEW_RELIC_GRAPH_TASK_PARAMS_METRIC_TYPE_VALUES: set[SnapshotNewRelicGraphTaskParamsMetricType] = {
    "APDEX",
    "AREA",
    "BAR",
    "BASELINE",
    "BILLBOARD",
    "BULLET",
    "EVENT_FEED",
    "FUNNEL",
    "HEATMAP",
    "HISTOGRAM",
    "LINE",
    "PIE",
    "SCATTER",
    "STACKED_HORIZONTAL_BAR",
    "TABLE",
    "VERTICAL_BAR",
}


def check_snapshot_new_relic_graph_task_params_metric_type(
    value: str | None,
) -> SnapshotNewRelicGraphTaskParamsMetricType | None:
    if value is None:
        return None
    if value in SNAPSHOT_NEW_RELIC_GRAPH_TASK_PARAMS_METRIC_TYPE_VALUES:
        return cast(SnapshotNewRelicGraphTaskParamsMetricType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SNAPSHOT_NEW_RELIC_GRAPH_TASK_PARAMS_METRIC_TYPE_VALUES!r}"
    )
