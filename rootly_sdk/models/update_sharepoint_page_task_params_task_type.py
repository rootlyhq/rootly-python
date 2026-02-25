from typing import Literal, cast

UpdateSharepointPageTaskParamsTaskType = Literal["update_sharepoint_page"]

UPDATE_SHAREPOINT_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateSharepointPageTaskParamsTaskType] = {
    "update_sharepoint_page",
}


def check_update_sharepoint_page_task_params_task_type(
    value: str | None,
) -> UpdateSharepointPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_SHAREPOINT_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateSharepointPageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SHAREPOINT_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
