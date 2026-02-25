from typing import Literal, cast

CreatePagerdutyStatusUpdateTaskParamsTaskType = Literal["create_pagerduty_status_update"]

CREATE_PAGERDUTY_STATUS_UPDATE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreatePagerdutyStatusUpdateTaskParamsTaskType] = {
    "create_pagerduty_status_update",
}


def check_create_pagerduty_status_update_task_params_task_type(
    value: str | None,
) -> CreatePagerdutyStatusUpdateTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_PAGERDUTY_STATUS_UPDATE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreatePagerdutyStatusUpdateTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PAGERDUTY_STATUS_UPDATE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
