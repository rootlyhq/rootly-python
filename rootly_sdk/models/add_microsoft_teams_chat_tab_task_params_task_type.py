from typing import Literal, cast

AddMicrosoftTeamsChatTabTaskParamsTaskType = Literal["add_microsoft_teams_chat_tab"]

ADD_MICROSOFT_TEAMS_CHAT_TAB_TASK_PARAMS_TASK_TYPE_VALUES: set[AddMicrosoftTeamsChatTabTaskParamsTaskType] = {
    "add_microsoft_teams_chat_tab",
}


def check_add_microsoft_teams_chat_tab_task_params_task_type(
    value: str | None,
) -> AddMicrosoftTeamsChatTabTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ADD_MICROSOFT_TEAMS_CHAT_TAB_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(AddMicrosoftTeamsChatTabTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_MICROSOFT_TEAMS_CHAT_TAB_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
