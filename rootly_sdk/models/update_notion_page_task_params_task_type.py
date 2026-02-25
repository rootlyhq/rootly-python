from typing import Literal, cast

UpdateNotionPageTaskParamsTaskType = Literal["update_notion_page"]

UPDATE_NOTION_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateNotionPageTaskParamsTaskType] = {
    "update_notion_page",
}


def check_update_notion_page_task_params_task_type(value: str | None) -> UpdateNotionPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_NOTION_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateNotionPageTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_NOTION_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
