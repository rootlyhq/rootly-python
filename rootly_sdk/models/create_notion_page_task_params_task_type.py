from typing import Literal, cast

CreateNotionPageTaskParamsTaskType = Literal["create_notion_page"]

CREATE_NOTION_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateNotionPageTaskParamsTaskType] = {
    "create_notion_page",
}


def check_create_notion_page_task_params_task_type(value: str | None) -> CreateNotionPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_NOTION_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateNotionPageTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_NOTION_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
