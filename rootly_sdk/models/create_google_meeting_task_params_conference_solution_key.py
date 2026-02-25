from typing import Literal, cast

CreateGoogleMeetingTaskParamsConferenceSolutionKey = Literal[
    "addOn", "eventHangout", "eventNamedHangout", "hangoutsMeet"
]

CREATE_GOOGLE_MEETING_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES: set[
    CreateGoogleMeetingTaskParamsConferenceSolutionKey
] = {
    "addOn",
    "eventHangout",
    "eventNamedHangout",
    "hangoutsMeet",
}


def check_create_google_meeting_task_params_conference_solution_key(
    value: str | None,
) -> CreateGoogleMeetingTaskParamsConferenceSolutionKey | None:
    if value is None:
        return None
    if value in CREATE_GOOGLE_MEETING_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES:
        return cast(CreateGoogleMeetingTaskParamsConferenceSolutionKey, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GOOGLE_MEETING_TASK_PARAMS_CONFERENCE_SOLUTION_KEY_VALUES!r}"
    )
