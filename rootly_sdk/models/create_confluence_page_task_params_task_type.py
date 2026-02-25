from typing import Literal, cast

CreateConfluencePageTaskParamsTaskType = Literal["create_confluence_page"]

CREATE_CONFLUENCE_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateConfluencePageTaskParamsTaskType] = {
    "create_confluence_page",
}


def check_create_confluence_page_task_params_task_type(value: str | None) -> CreateConfluencePageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_CONFLUENCE_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateConfluencePageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONFLUENCE_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
