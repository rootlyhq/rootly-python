from typing import Literal, cast

CreateGoogleChatSpaceTaskParamsTaskType = Literal["create_google_chat_space"]

CREATE_GOOGLE_CHAT_SPACE_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGoogleChatSpaceTaskParamsTaskType] = {
    "create_google_chat_space",
}


def check_create_google_chat_space_task_params_task_type(
    value: str | None,
) -> CreateGoogleChatSpaceTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_CHAT_SPACE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGoogleChatSpaceTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_CHAT_SPACE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
