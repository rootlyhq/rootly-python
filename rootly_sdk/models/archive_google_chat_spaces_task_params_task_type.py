from typing import Literal, cast

ArchiveGoogleChatSpacesTaskParamsTaskType = Literal["archive_google_chat_spaces"]

ARCHIVE_GOOGLE_CHAT_SPACES_TASK_PARAMS_TASK_TYPE_VALUES: set[ArchiveGoogleChatSpacesTaskParamsTaskType] = {
    "archive_google_chat_spaces",
}


def check_archive_google_chat_spaces_task_params_task_type(
    value: str | None,
) -> ArchiveGoogleChatSpacesTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ARCHIVE_GOOGLE_CHAT_SPACES_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(ArchiveGoogleChatSpacesTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARCHIVE_GOOGLE_CHAT_SPACES_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
