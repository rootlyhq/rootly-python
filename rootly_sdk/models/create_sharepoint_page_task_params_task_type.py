from typing import Literal, cast

CreateSharepointPageTaskParamsTaskType = Literal["create_sharepoint_page"]

CREATE_SHAREPOINT_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateSharepointPageTaskParamsTaskType] = {
    "create_sharepoint_page",
}


def check_create_sharepoint_page_task_params_task_type(value: str | None) -> CreateSharepointPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_SHAREPOINT_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateSharepointPageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_SHAREPOINT_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
