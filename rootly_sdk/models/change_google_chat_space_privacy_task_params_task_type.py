from typing import Literal

ChangeGoogleChatSpacePrivacyTaskParamsTaskType = Literal["change_google_chat_space_privacy"]

CHANGE_GOOGLE_CHAT_SPACE_PRIVACY_TASK_PARAMS_TASK_TYPE_VALUES: set[ChangeGoogleChatSpacePrivacyTaskParamsTaskType] = {
    "change_google_chat_space_privacy",
}


def check_change_google_chat_space_privacy_task_params_task_type(
    value: str | None,
) -> ChangeGoogleChatSpacePrivacyTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CHANGE_GOOGLE_CHAT_SPACE_PRIVACY_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHANGE_GOOGLE_CHAT_SPACE_PRIVACY_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
