from typing import Literal, cast

UpdateCodaPageTaskParamsTaskType = Literal["update_coda_page"]

UPDATE_CODA_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateCodaPageTaskParamsTaskType] = {
    "update_coda_page",
}


def check_update_coda_page_task_params_task_type(value: str | None) -> UpdateCodaPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_CODA_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateCodaPageTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CODA_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
