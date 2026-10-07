from typing import Literal

RemoveFromSlackChannelTaskParamsTargetKind = Literal["users_without_private_incident_access"]

REMOVE_FROM_SLACK_CHANNEL_TASK_PARAMS_TARGET_KIND_VALUES: set[RemoveFromSlackChannelTaskParamsTargetKind] = {
    "users_without_private_incident_access",
}


def check_remove_from_slack_channel_task_params_target_kind(
    value: str | None,
) -> RemoveFromSlackChannelTaskParamsTargetKind | None:
    if value is None:
        return None
    if value in REMOVE_FROM_SLACK_CHANNEL_TASK_PARAMS_TARGET_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_FROM_SLACK_CHANNEL_TASK_PARAMS_TARGET_KIND_VALUES!r}"
    )
