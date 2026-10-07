from typing import Literal

GetMeetingRecordingInclude = Literal["transcript"]

GET_MEETING_RECORDING_INCLUDE_VALUES: set[GetMeetingRecordingInclude] = {
    "transcript",
}


def check_get_meeting_recording_include(value: str | None) -> GetMeetingRecordingInclude | None:
    if value is None:
        return None
    if value in GET_MEETING_RECORDING_INCLUDE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MEETING_RECORDING_INCLUDE_VALUES!r}")
