from typing import Literal, cast

CreateOpenaiChatCompletionTaskParamsReasoningSummary = Literal["auto", "concise", "detailed"]

CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_REASONING_SUMMARY_VALUES: set[
    CreateOpenaiChatCompletionTaskParamsReasoningSummary
] = {
    "auto",
    "concise",
    "detailed",
}


def check_create_openai_chat_completion_task_params_reasoning_summary(
    value: str,
) -> CreateOpenaiChatCompletionTaskParamsReasoningSummary:
    if value in CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_REASONING_SUMMARY_VALUES:
        return cast(CreateOpenaiChatCompletionTaskParamsReasoningSummary, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_REASONING_SUMMARY_VALUES!r}"
    )
