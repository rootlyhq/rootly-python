from typing import Literal, cast

TweetTwitterMessageTaskParamsTaskType = Literal["tweet_twitter_message"]

TWEET_TWITTER_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[TweetTwitterMessageTaskParamsTaskType] = {
    "tweet_twitter_message",
}


def check_tweet_twitter_message_task_params_task_type(
    value: str | None,
) -> TweetTwitterMessageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in TWEET_TWITTER_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(TweetTwitterMessageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TWEET_TWITTER_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
