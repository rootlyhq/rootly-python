from typing import Literal, cast

SendGoogleChatMessageTaskParamsTaskType = Literal["send_google_chat_message"]

SEND_GOOGLE_CHAT_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[SendGoogleChatMessageTaskParamsTaskType] = {
    "send_google_chat_message",
}


def check_send_google_chat_message_task_params_task_type(
    value: str | None,
) -> SendGoogleChatMessageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SEND_GOOGLE_CHAT_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SendGoogleChatMessageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEND_GOOGLE_CHAT_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
