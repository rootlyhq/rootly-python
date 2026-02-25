from typing import Literal, cast

CreateMicrosoftTeamsChannelTaskParamsTaskType = Literal["create_microsoft_teams_channel"]

CREATE_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateMicrosoftTeamsChannelTaskParamsTaskType] = {
    "create_microsoft_teams_channel",
}


def check_create_microsoft_teams_channel_task_params_task_type(
    value: str | None,
) -> CreateMicrosoftTeamsChannelTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateMicrosoftTeamsChannelTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
