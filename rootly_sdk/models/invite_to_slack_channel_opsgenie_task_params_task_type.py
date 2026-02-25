from typing import Literal, cast

InviteToSlackChannelOpsgenieTaskParamsTaskType = Literal["invite_to_slack_channel_opsgenie"]

INVITE_TO_SLACK_CHANNEL_OPSGENIE_TASK_PARAMS_TASK_TYPE_VALUES: set[InviteToSlackChannelOpsgenieTaskParamsTaskType] = {
    "invite_to_slack_channel_opsgenie",
}


def check_invite_to_slack_channel_opsgenie_task_params_task_type(
    value: str | None,
) -> InviteToSlackChannelOpsgenieTaskParamsTaskType | None:
    if value is None:
        return None
    if value in INVITE_TO_SLACK_CHANNEL_OPSGENIE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(InviteToSlackChannelOpsgenieTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVITE_TO_SLACK_CHANNEL_OPSGENIE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
