from typing import Literal, cast

CreateMistralChatCompletionTaskParamsTaskType = Literal["create_mistral_chat_completion_task"]

CREATE_MISTRAL_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateMistralChatCompletionTaskParamsTaskType] = {
    "create_mistral_chat_completion_task",
}


def check_create_mistral_chat_completion_task_params_task_type(
    value: str | None,
) -> CreateMistralChatCompletionTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_MISTRAL_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateMistralChatCompletionTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MISTRAL_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
