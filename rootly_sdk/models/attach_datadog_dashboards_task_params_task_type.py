from typing import Literal, cast

AttachDatadogDashboardsTaskParamsTaskType = Literal["attach_datadog_dashboards"]

ATTACH_DATADOG_DASHBOARDS_TASK_PARAMS_TASK_TYPE_VALUES: set[AttachDatadogDashboardsTaskParamsTaskType] = {
    "attach_datadog_dashboards",
}


def check_attach_datadog_dashboards_task_params_task_type(value: str | None) -> AttachDatadogDashboardsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ATTACH_DATADOG_DASHBOARDS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AttachDatadogDashboardsTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ATTACH_DATADOG_DASHBOARDS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
