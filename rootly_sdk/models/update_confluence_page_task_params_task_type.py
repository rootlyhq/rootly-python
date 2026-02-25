from typing import Literal, cast

UpdateConfluencePageTaskParamsTaskType = Literal["update_confluence_page"]

UPDATE_CONFLUENCE_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateConfluencePageTaskParamsTaskType] = {
    "update_confluence_page",
}


def check_update_confluence_page_task_params_task_type(
    value: str | None,
) -> UpdateConfluencePageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_CONFLUENCE_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateConfluencePageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CONFLUENCE_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
