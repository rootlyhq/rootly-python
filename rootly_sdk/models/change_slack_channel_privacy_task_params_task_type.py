from typing import Literal, cast

ChangeSlackChannelPrivacyTaskParamsTaskType = Literal["rename_slack_channel"]

CHANGE_SLACK_CHANNEL_PRIVACY_TASK_PARAMS_TASK_TYPE_VALUES: set[ChangeSlackChannelPrivacyTaskParamsTaskType] = {
    "rename_slack_channel",
}


def check_change_slack_channel_privacy_task_params_task_type(value: str | None) -> ChangeSlackChannelPrivacyTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CHANGE_SLACK_CHANNEL_PRIVACY_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(ChangeSlackChannelPrivacyTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHANGE_SLACK_CHANNEL_PRIVACY_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
