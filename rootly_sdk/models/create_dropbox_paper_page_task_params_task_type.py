from typing import Literal, cast

CreateDropboxPaperPageTaskParamsTaskType = Literal["create_dropbox_paper_page"]

CREATE_DROPBOX_PAPER_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateDropboxPaperPageTaskParamsTaskType] = {
    "create_dropbox_paper_page",
}


def check_create_dropbox_paper_page_task_params_task_type(value: str | None) -> CreateDropboxPaperPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_DROPBOX_PAPER_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateDropboxPaperPageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_DROPBOX_PAPER_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
