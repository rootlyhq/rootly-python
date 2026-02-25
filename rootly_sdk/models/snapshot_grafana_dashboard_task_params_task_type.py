from typing import Literal, cast

SnapshotGrafanaDashboardTaskParamsTaskType = Literal["snapshot_grafana_dashboard"]

SNAPSHOT_GRAFANA_DASHBOARD_TASK_PARAMS_TASK_TYPE_VALUES: set[SnapshotGrafanaDashboardTaskParamsTaskType] = {
    "snapshot_grafana_dashboard",
}


def check_snapshot_grafana_dashboard_task_params_task_type(
    value: str | None,
) -> SnapshotGrafanaDashboardTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SNAPSHOT_GRAFANA_DASHBOARD_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SnapshotGrafanaDashboardTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SNAPSHOT_GRAFANA_DASHBOARD_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
