from typing import Literal, cast

CreateGoogleDocsPageTaskParamsTaskType = Literal["create_google_docs_page"]

CREATE_GOOGLE_DOCS_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGoogleDocsPageTaskParamsTaskType] = {
    "create_google_docs_page",
}


def check_create_google_docs_page_task_params_task_type(value: str | None) -> CreateGoogleDocsPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_DOCS_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGoogleDocsPageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_DOCS_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
