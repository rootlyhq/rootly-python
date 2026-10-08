from typing import Literal

CreateSlackChannelTaskParamsPrivate = Literal["auto", "false", "true"]

CREATE_SLACK_CHANNEL_TASK_PARAMS_PRIVATE_VALUES: set[CreateSlackChannelTaskParamsPrivate] = {
    "auto",
    "false",
    "true",
}


def check_create_slack_channel_task_params_private(value: str | None) -> CreateSlackChannelTaskParamsPrivate | None:
    if value is None:
        return None
    if value in CREATE_SLACK_CHANNEL_TASK_PARAMS_PRIVATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_SLACK_CHANNEL_TASK_PARAMS_PRIVATE_VALUES!r}")
