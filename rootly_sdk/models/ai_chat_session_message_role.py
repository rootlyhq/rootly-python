from typing import Literal, cast

AiChatSessionMessageRole = Literal["assistant", "user"]

AI_CHAT_SESSION_MESSAGE_ROLE_VALUES: set[AiChatSessionMessageRole] = {
    "assistant",
    "user",
}


def check_ai_chat_session_message_role(value: str | None) -> AiChatSessionMessageRole | None:
    if value is None:
        return None
    if value in AI_CHAT_SESSION_MESSAGE_ROLE_VALUES:
        return cast(AiChatSessionMessageRole, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AI_CHAT_SESSION_MESSAGE_ROLE_VALUES!r}")
