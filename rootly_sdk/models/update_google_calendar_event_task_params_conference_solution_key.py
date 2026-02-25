from typing import Literal, cast

UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey = Literal[
    "addOn", "eventHangout", "eventNamedHangout", "hangoutsMeet"
]

UPDATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES: set[
    UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey
] = {
    "addOn",
    "eventHangout",
    "eventNamedHangout",
    "hangoutsMeet",
}


def check_update_google_calendar_event_task_params_conference_solution_key(
    value: str | None,
) -> UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey | None:
    if value is None:
        return None
    if value in UPDATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES:
        return cast(UpdateGoogleCalendarEventTaskParamsConferenceSolutionKey, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_GOOGLE_CALENDAR_EVENT_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES!r}"
    )
