from typing import Literal

AiChatResponseDataType = Literal["ai_chat_responses"]

AI_CHAT_RESPONSE_DATA_TYPE_VALUES: set[AiChatResponseDataType] = {
    "ai_chat_responses",
}


def check_ai_chat_response_data_type(value: str | None) -> AiChatResponseDataType | None:
    if value is None:
        return None
    if value in AI_CHAT_RESPONSE_DATA_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AI_CHAT_RESPONSE_DATA_TYPE_VALUES!r}")
