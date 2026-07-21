from typing import Literal, cast

RenameGoogleChatSpaceTaskParamsTaskType = Literal["rename_google_chat_space"]

RENAME_GOOGLE_CHAT_SPACE_TASK_PARAMS_TASK_TYPE_VALUES: set[RenameGoogleChatSpaceTaskParamsTaskType] = {
    "rename_google_chat_space",
}


def check_rename_google_chat_space_task_params_task_type(
    value: str | None,
) -> RenameGoogleChatSpaceTaskParamsTaskType | None:
    if value is None:
        return None
    if value in RENAME_GOOGLE_CHAT_SPACE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(RenameGoogleChatSpaceTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RENAME_GOOGLE_CHAT_SPACE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
