from typing import Literal, cast

UpdateSlackChannelTopicTaskParamsTaskType = Literal["update_slack_channel_topic"]

UPDATE_SLACK_CHANNEL_TOPIC_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateSlackChannelTopicTaskParamsTaskType] = {
    "update_slack_channel_topic",
}


def check_update_slack_channel_topic_task_params_task_type(value: str | None) -> UpdateSlackChannelTopicTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_SLACK_CHANNEL_TOPIC_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateSlackChannelTopicTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_SLACK_CHANNEL_TOPIC_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
