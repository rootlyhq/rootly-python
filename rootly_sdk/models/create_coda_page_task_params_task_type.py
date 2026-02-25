from typing import Literal, cast

CreateCodaPageTaskParamsTaskType = Literal["create_coda_page"]

CREATE_CODA_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateCodaPageTaskParamsTaskType] = {
    "create_coda_page",
}


def check_create_coda_page_task_params_task_type(value: str | None) -> CreateCodaPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_CODA_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateCodaPageTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_CODA_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
