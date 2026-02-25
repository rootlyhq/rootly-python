from typing import Literal, cast

SendWhatsappMessageTaskParamsTaskType = Literal["send_whatsapp_message"]

SEND_WHATSAPP_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES: set[SendWhatsappMessageTaskParamsTaskType] = {
    "send_whatsapp_message",
}


def check_send_whatsapp_message_task_params_task_type(
    value: str | None,
) -> SendWhatsappMessageTaskParamsTaskType | None:
    if value is None:
        return None
    if value in SEND_WHATSAPP_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(SendWhatsappMessageTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEND_WHATSAPP_MESSAGE_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
