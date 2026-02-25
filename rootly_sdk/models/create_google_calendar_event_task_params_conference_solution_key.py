from typing import Literal, cast

CreateGoogleCalendarEventTaskParamsConferenceSolutionKey = Literal[
    "addOn", "eventHangout", "eventNamedHangout", "hangoutsMeet"
]

CREATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES: set[
    CreateGoogleCalendarEventTaskParamsConferenceSolutionKey
] = {
    "addOn",
    "eventHangout",
    "eventNamedHangout",
    "hangoutsMeet",
}


def check_create_google_calendar_event_task_params_conference_solution_key(
    value: str | None,
) -> CreateGoogleCalendarEventTaskParamsConferenceSolutionKey | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES:
        return cast(CreateGoogleCalendarEventTaskParamsConferenceSolutionKey, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES!r}"
    )
