from typing import Literal, cast

CreateQuipPageTaskParamsTaskType = Literal["create_google_docs_page"]

CREATE_QUIP_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateQuipPageTaskParamsTaskType] = {
    "create_google_docs_page",
}


def check_create_quip_page_task_params_task_type(value: str | None) -> CreateQuipPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_QUIP_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateQuipPageTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_QUIP_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}")
