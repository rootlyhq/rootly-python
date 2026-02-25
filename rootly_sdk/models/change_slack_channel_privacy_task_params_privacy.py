from typing import Literal, cast

ChangeSlackChannelPrivacyTaskParamsPrivacy = Literal["private", "public"]

CHANGE_SLACK_CHANNEL_PRIVACY_TASK_PARAMS_PRIVACY_VALUES: set[ChangeSlackChannelPrivacyTaskParamsPrivacy] = {
    "private",
    "public",
}


def check_change_slack_channel_privacy_task_params_privacy(
    value: str | None,
) -> ChangeSlackChannelPrivacyTaskParamsPrivacy | None:
    if value is None:
        return None
    if value in CHANGE_SLACK_CHANNEL_PRIVACY_TASK_PARAMS_PRIVACY_VALUES:
        return cast(ChangeSlackChannelPrivacyTaskParamsPrivacy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHANGE_SLACK_CHANNEL_PRIVACY_TASK_PARAMS_PRIVACY_VALUES!r}"
    )
