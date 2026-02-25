from typing import Literal, cast

UpdateGoogleDocsPageTaskParamsTaskType = Literal["update_google_docs_page"]

UPDATE_GOOGLE_DOCS_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateGoogleDocsPageTaskParamsTaskType] = {
    "update_google_docs_page",
}


def check_update_google_docs_page_task_params_task_type(
    value: str | None,
) -> UpdateGoogleDocsPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_GOOGLE_DOCS_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateGoogleDocsPageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_GOOGLE_DOCS_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
