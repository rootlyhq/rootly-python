from typing import Literal, cast

RenameMicrosoftTeamsChannelTaskParamsTaskType = Literal["rename_microsoft_teams_channel"]

RENAME_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES: set[RenameMicrosoftTeamsChannelTaskParamsTaskType] = {
    "rename_microsoft_teams_channel",
}


def check_rename_microsoft_teams_channel_task_params_task_type(
    value: str | None,
) -> RenameMicrosoftTeamsChannelTaskParamsTaskType | None:
    if value is None:
        return None
    if value in RENAME_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(RenameMicrosoftTeamsChannelTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RENAME_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
