from typing import Literal, cast

SendEmailTaskParamsTaskType = Literal["send_email"]

SEND_EMAIL_TASK_PARAMS_TASK_TYPE_VALUES: set[SendEmailTaskParamsTaskType] = {
    "send_email",
}


def check_send_email_task_params_task_type(value: str | None) -> SendEmailTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SEND_EMAIL_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SendEmailTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEND_EMAIL_TASK_PARAMS_TASK_TYPE_VALUES!r}")
