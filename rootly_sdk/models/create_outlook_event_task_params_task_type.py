from typing import Literal, cast

CreateOutlookEventTaskParamsTaskType = Literal["create_outlook_event"]

CREATE_OUTLOOK_EVENT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateOutlookEventTaskParamsTaskType] = {
    "create_outlook_event",
}


def check_create_outlook_event_task_params_task_type(value: str | None) -> CreateOutlookEventTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_OUTLOOK_EVENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateOutlookEventTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_OUTLOOK_EVENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
