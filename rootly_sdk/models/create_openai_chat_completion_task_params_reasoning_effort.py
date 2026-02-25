from typing import Literal, cast

CreateOpenaiChatCompletionTaskParamsReasoningEffort = Literal["high", "low", "medium", "minimal"]

CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_REASONING_EFFORT_VALUES: set[
    CreateOpenaiChatCompletionTaskParamsReasoningEffort
] = {
    "high",
    "low",
    "medium",
    "minimal",
}


def check_create_openai_chat_completion_task_params_reasoning_effort(
    value: str | None,
) -> CreateOpenaiChatCompletionTaskParamsReasoningEffort | None:
    if value is None:
        return None
    if value in CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_REASONING_EFFORT_VALUES:
        return cast(CreateOpenaiChatCompletionTaskParamsReasoningEffort, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_REASONING_EFFORT_VALUES!r}"
    )
