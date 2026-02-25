from typing import Literal, cast

CreateMicrosoftTeamsChannelTaskParamsPrivate = Literal["auto", "false", "true"]

CREATE_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_PRIVATE_VALUES: set[CreateMicrosoftTeamsChannelTaskParamsPrivate] = {
    "auto",
    "false",
    "true",
}


def check_create_microsoft_teams_channel_task_params_private(
    value: str | None,
) -> CreateMicrosoftTeamsChannelTaskParamsPrivate | None:
    if value is None:
        return None
    if value in CREATE_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_PRIVATE_VALUES:
        return cast(CreateMicrosoftTeamsChannelTaskParamsPrivate, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_MICROSOFT_TEAMS_CHANNEL_TASK_PARAMS_PRIVATE_VALUES!r}"
    )
