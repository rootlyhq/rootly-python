from typing import Literal, cast

CreateWatsonxChatCompletionTaskParamsTaskType = Literal["create_watsonx_chat_completion_task"]

CREATE_WATSONX_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateWatsonxChatCompletionTaskParamsTaskType] = {
    "create_watsonx_chat_completion_task",
}


def check_create_watsonx_chat_completion_task_params_task_type(
    value: str | None,
) -> CreateWatsonxChatCompletionTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_WATSONX_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateWatsonxChatCompletionTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_WATSONX_CHAT_COMPLETION_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
