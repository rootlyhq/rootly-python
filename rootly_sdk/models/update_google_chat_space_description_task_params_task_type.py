from typing import Literal

UpdateGoogleChatSpaceDescriptionTaskParamsTaskType = Literal["update_google_chat_space_description"]

UPDATE_GOOGLE_CHAT_SPACE_DESCRIPTION_TASK_PARAMS_TASK_TYPE_VALUES: set[
    UpdateGoogleChatSpaceDescriptionTaskParamsTaskType
] = {
    "update_google_chat_space_description",
}


def check_update_google_chat_space_description_task_params_task_type(
    value: str | None,
) -> UpdateGoogleChatSpaceDescriptionTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_GOOGLE_CHAT_SPACE_DESCRIPTION_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_GOOGLE_CHAT_SPACE_DESCRIPTION_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
