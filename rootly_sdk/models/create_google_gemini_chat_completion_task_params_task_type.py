from typing import Literal, cast

CreateGoogleGeminiChatCompletionTaskParamsTaskType = Literal["create_google_gemini_chat_completion_task"]

CREATE_GOOGLE_GEMINI_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES: set[
    CreateGoogleGeminiChatCompletionTaskParamsTaskType
] = {
    "create_google_gemini_chat_completion_task",
}


def check_create_google_gemini_chat_completion_task_params_task_type(
    value: str | None,
) -> CreateGoogleGeminiChatCompletionTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_GEMINI_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGoogleGeminiChatCompletionTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_GEMINI_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
