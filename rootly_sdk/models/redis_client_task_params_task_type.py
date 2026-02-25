from typing import Literal, cast

RedisClientTaskParamsTaskType = Literal["redis_client"]

REDIS_CLIENT_TASK_PARAMS_TASK_TYPE_VALUES: set[RedisClientTaskParamsTaskType] = {
    "redis_client",
}


def check_redis_client_task_params_task_type(value: str | None) -> RedisClientTaskParamsTaskType | None:
    if value is None:
        return None
    if value in REDIS_CLIENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(RedisClientTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REDIS_CLIENT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
