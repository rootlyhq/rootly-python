from typing import Literal, cast

CreateGoogleCalendarEventTaskParamsTaskType = Literal["create_google_calendar_event"]

CREATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_TASK_TYPE_VALUES: set[CreateGoogleCalendarEventTaskParamsTaskType] = {
    "create_google_calendar_event",
}


def check_create_google_calendar_event_task_params_task_type(value: str | None) -> CreateGoogleCalendarEventTaskParamsTaskType | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(CreateGoogleCalendarEventTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
