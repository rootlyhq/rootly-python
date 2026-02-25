from typing import Literal, cast

ArchiveMicrosoftTeamsChannelsTaskParamsTaskType = Literal["archive_microsoft_teams_channels"]

ARCHIVE_MICROSOFT_TEAMS_CHANNELS_TASK_PARAMS_TASK_TYPE_VALUES: set[ArchiveMicrosoftTeamsChannelsTaskParamsTaskType] = {
    "archive_microsoft_teams_channels",
}


def check_archive_microsoft_teams_channels_task_params_task_type(
    value: str | None,
) -> ArchiveMicrosoftTeamsChannelsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in ARCHIVE_MICROSOFT_TEAMS_CHANNELS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(ArchiveMicrosoftTeamsChannelsTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARCHIVE_MICROSOFT_TEAMS_CHANNELS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
