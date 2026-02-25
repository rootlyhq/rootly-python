from typing import Literal, cast

UpdateGoogleCalendarEventTaskParamsTaskType = Literal["create_google_calendar_event"]

UPDATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_TASK_TYPE_VALUES: set[UpdateGoogleCalendarEventTaskParamsTaskType] = {
    "create_google_calendar_event",
}


def check_update_google_calendar_event_task_params_task_type(value: str | None) -> UpdateGoogleCalendarEventTaskParamsTaskType | None:
    if value is None:
        return None
    if value in UPDATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_TASK_TYPE_VALUES:
        return cast(UpdateGoogleCalendarEventTaskParamsTaskType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_TASK_TYPE_VALUES!r}"
    )
