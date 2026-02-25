from typing import Literal, cast

SendSmsTaskParamsTaskType = Literal["send_sms"]

SEND_SMS_TASK_PARAMS_TASK_TYPE_VALUES: set[SendSmsTaskParamsTaskType] = {
    "send_sms",
}


def check_send_sms_task_params_task_type(value: str | None) -> SendSmsTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SEND_SMS_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SendSmsTaskParamsTaskType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEND_SMS_TASK_PARAMS_TASK_TYPE_VALUES!r}")
