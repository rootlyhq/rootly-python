from typing import Literal

RemoveFromSlackChannelTaskParamsTaskType = Literal["remove_from_slack_channel"]

REMOVE_FROM_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES: set[RemoveFromSlackChannelTaskParamsTaskType] = {
    "remove_from_slack_channel",
}


def check_remove_from_slack_channel_task_params_task_type(
    value: str | None,
) -> RemoveFromSlackChannelTaskParamsTaskType | None:
    if value is None:
        return None
    if value in REMOVE_FROM_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_FROM_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
