from typing import Literal, cast

CreateAnthropicChatCompletionTaskParamsTaskType = Literal["create_anthropic_chat_completion_task"]

CREATE_ANTHROPIC_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateAnthropicChatCompletionTaskParamsTaskType] = {
    "create_anthropic_chat_completion_task",
}


def check_create_anthropic_chat_completion_task_params_task_type(
    value: str | None,
) -> CreateAnthropicChatCompletionTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_ANTHROPIC_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateAnthropicChatCompletionTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_ANTHROPIC_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
