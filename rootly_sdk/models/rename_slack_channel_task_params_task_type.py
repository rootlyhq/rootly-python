from typing import Literal, cast

RenameSlackChannelTaskParamsTaskType = Literal["rename_slack_channel"]

RENAME_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES: set[RenameSlackChannelTaskParamsTaskType] = {
    "rename_slack_channel",
}


def check_rename_slack_channel_task_params_task_type(value: str | None) -> RenameSlackChannelTaskParamsTaskType | None:
    if value is None:
        return None
    if value in RENAME_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(RenameSlackChannelTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RENAME_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
