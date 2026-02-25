from typing import Literal, cast

CreateMicrosoftTeamsChatTaskParamsTaskType = Literal["create_microsoft_teams_chat"]

CREATE_MICROSOFT_TEAMS_CHAT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateMicrosoftTeamsChatTaskParamsTaskType] = {
    "create_microsoft_teams_chat",
}


def check_create_microsoft_teams_chat_task_params_task_type(value: str | None) -> CreateMicrosoftTeamsChatTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_MICROSOFT_TEAMS_CHAT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateMicrosoftTeamsChatTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MICROSOFT_TEAMS_CHAT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
