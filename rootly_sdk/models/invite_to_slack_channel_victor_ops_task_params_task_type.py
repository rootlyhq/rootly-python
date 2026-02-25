from typing import Literal, cast

InviteToSlackChannelVictorOpsTaskParamsTaskType = Literal["invite_to_slack_channel_victor_ops"]

INVITE_TO_SLACK_CHANNEL_VICTOR_OPS_TASK_PARAMS_TASK_TYPE_VALUES: set[
    InviteToSlackChannelVictorOpsTaskParamsTaskType
] = {
    "invite_to_slack_channel_victor_ops",
}


def check_invite_to_slack_channel_victor_ops_task_params_task_type(
    value: str | None,
) -> InviteToSlackChannelVictorOpsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in INVITE_TO_SLACK_CHANNEL_VICTOR_OPS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(InviteToSlackChannelVictorOpsTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVITE_TO_SLACK_CHANNEL_VICTOR_OPS_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
