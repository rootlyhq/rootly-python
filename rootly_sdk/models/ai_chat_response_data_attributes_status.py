from typing import Literal

AiChatResponseDataAttributesStatus = Literal["user_input_required"]

AI_CHAT_RESPONSE_DATA_ATTRIBUTES_STATUS_VALUES: set[AiChatResponseDataAttributesStatus] = {
    "user_input_required",
}


def check_ai_chat_response_data_attributes_status(value: str | None) -> AiChatResponseDataAttributesStatus | None:
    if value is None:
        return None
    if value in AI_CHAT_RESPONSE_DATA_ATTRIBUTES_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AI_CHAT_RESPONSE_DATA_ATTRIBUTES_STATUS_VALUES!r}")
