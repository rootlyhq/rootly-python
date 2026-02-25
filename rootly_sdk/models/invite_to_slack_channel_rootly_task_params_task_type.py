from typing import Literal, cast

InviteToSlackChannelRootlyTaskParamsTaskType = Literal["invite_to_slack_channel_rootly"]

INVITE_TO_SLACK_CHANNEL_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES: set[InviteToSlackChannelRootlyTaskParamsTaskType] = {
    "invite_to_slack_channel_rootly",
}


def check_invite_to_slack_channel_rootly_task_params_task_type(
    value: str | None,
) -> InviteToSlackChannelRootlyTaskParamsTaskType | None:
    if value is None:
        return None
    if value in INVITE_TO_SLACK_CHANNEL_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(InviteToSlackChannelRootlyTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVITE_TO_SLACK_CHANNEL_ROOTLY_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
