from typing import Literal, cast

UpdateDropboxPaperPageTaskParamsTaskType = Literal["update_dropbox_paper_page"]

UPDATE_DROPBOX_PAPER_PAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateDropboxPaperPageTaskParamsTaskType] = {
    "update_dropbox_paper_page",
}


def check_update_dropbox_paper_page_task_params_task_type(
    value: str | None,
) -> UpdateDropboxPaperPageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_DROPBOX_PAPER_PAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateDropboxPaperPageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_DROPBOX_PAPER_PAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
