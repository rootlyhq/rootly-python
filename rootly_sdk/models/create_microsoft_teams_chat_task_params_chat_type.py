from typing import Literal, cast

CreateMicrosoftTeamsChatTaskParamsChatType = Literal["group", "oneOnOne"]

CREATE_MICROSOFT_TEAMS_CHAT_TASK_PARAMS_CHAT_TYPE_VALUES: set[CreateMicrosoftTeamsChatTaskParamsChatType] = {
    "group",
    "oneOnOne",
}


def check_create_microsoft_teams_chat_task_params_chat_type(
    value: str | None,
) -> CreateMicrosoftTeamsChatTaskParamsChatType | None:
    if value is None:
        return None
    if value in CREATE_MICROSOFT_TEAMS_CHAT_TASK_PARAMS_CHAT_TYPE_VALUES:
        return cast(CreateMicrosoftTeamsChatTaskParamsChatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MICROSOFT_TEAMS_CHAT_TASK_PARAMS_CHAT_TYPE_VALUES!r}"
    )
