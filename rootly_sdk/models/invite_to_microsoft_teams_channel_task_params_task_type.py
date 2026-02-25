from typing import Literal, cast

InviteToMicrosoftTeamsChannelTaskParamsTaskType = Literal["invite_to_microsoft_teams_channel"]

INVITE_TO_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES: set[InviteToMicrosoftTeamsChannelTaskParamsTaskType] = {
    "invite_to_microsoft_teams_channel",
}


def check_invite_to_microsoft_teams_channel_task_params_task_type(
    value: str | None,
) -> InviteToMicrosoftTeamsChannelTaskParamsTaskType | None:
    if value is None:
        return None
    if value in INVITE_TO_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(InviteToMicrosoftTeamsChannelTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVITE_TO_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
