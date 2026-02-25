from typing import Literal, cast

SendDashboardReportTaskParamsTaskType = Literal["send_dashboard_report"]

SEND_DASHBOARD_REPORT_TASK_PARAMS_TASK_TYPE_VALUES: set[SendDashboardReportTaskParamsTaskType] = {
    "send_dashboard_report",
}


def check_send_dashboard_report_task_params_task_type(value: str | None) -> SendDashboardReportTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SEND_DASHBOARD_REPORT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SendDashboardReportTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEND_DASHBOARD_REPORT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
