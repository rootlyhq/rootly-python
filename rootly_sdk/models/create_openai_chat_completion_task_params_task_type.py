from typing import Literal, cast

CreateOpenaiChatCompletionTaskParamsTaskType = Literal["openai_chat_completion"]

CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateOpenaiChatCompletionTaskParamsTaskType] = {
    "openai_chat_completion",
}


def check_create_openai_chat_completion_task_params_task_type(
    value: str | None,
) -> CreateOpenaiChatCompletionTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateOpenaiChatCompletionTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_OPENAI_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
