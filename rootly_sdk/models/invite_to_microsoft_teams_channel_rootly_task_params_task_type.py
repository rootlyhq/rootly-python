from typing import Literal, cast

InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType = Literal["invite_to_microsoft_teams_channel_rootly"]

INVITE_TO_MICROSOFT_TEAMS_CHANNEL_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES: set[
    InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType
] = {
    "invite_to_microsoft_teams_channel_rootly",
}


def check_invite_to_microsoft_teams_channel_rootly_task_params_task_type(
    value: str | None,
) -> InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType | None:
    if value is None:
        return None
    if value in INVITE_TO_MICROSOFT_TEAMS_CHANNEL_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(InviteToMicrosoftTeamsChannelRootlyTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVITE_TO_MICROSOFT_TEAMS_CHANNEL_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
