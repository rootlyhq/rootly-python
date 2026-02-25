from typing import Literal, cast

SendMicrosoftTeamsChatMessageTaskParamsTaskType = Literal["send_microsoft_teams_chat_message"]

SEND_MICROSOFT_TEAMS_CHAT_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[SendMicrosoftTeamsChatMessageTaskParamsTaskType] = {
    "send_microsoft_teams_chat_message",
}


def check_send_microsoft_teams_chat_message_task_params_task_type(
    value: str | None,
) -> SendMicrosoftTeamsChatMessageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SEND_MICROSOFT_TEAMS_CHAT_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SendMicrosoftTeamsChatMessageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEND_MICROSOFT_TEAMS_CHAT_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
