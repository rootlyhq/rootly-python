from typing import Literal, cast

HttpClientTaskParamsTaskType = Literal["http_client"]

HTTP_CLIENT_TASK_PARAMS_TASK_TYPE_VALUES: set[HttpClientTaskParamsTaskType] = {
    "http_client",
}


def check_http_client_task_params_task_type(value: str | None) -> HttpClientTaskParamsTaskType | None:
    if value is None:
        return None
    if value in HTTP_CLIENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(HttpClientTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HTTP_CLIENT_TASK_PARAMS_TASK_TYPE_VALUES!r}")
