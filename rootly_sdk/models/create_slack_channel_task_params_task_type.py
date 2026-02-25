from typing import Literal, cast

CreateSlackChannelTaskParamsTaskType = Literal["create_slack_channel"]

CREATE_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateSlackChannelTaskParamsTaskType] = {
    "create_slack_channel",
}


def check_create_slack_channel_task_params_task_type(value: str | None) -> CreateSlackChannelTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateSlackChannelTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_SLACK_CHANNEL_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
