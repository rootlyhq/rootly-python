from typing import Literal, cast

UpdateQuipPageTaskParamsTaskType = Literal["update_quip_page"]

UPDATE_QUIP_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateQuipPageTaskParamsTaskType] = {
    "update_quip_page",
}


def check_update_quip_page_task_params_task_type(value: str | None) -> UpdateQuipPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_QUIP_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateQuipPageTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_QUIP_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
