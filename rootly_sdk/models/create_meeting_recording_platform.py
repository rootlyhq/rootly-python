from typing import Literal, cast

CreateMeetingRecordingPlatform = Literal["google_meet", "microsoft_teams", "webex", "zoom"]

CREATE_MEETING_RECORDING_PLATFORM_VALUES: set[CreateMeetingRecordingPlatform] = {
    "google_meet",
    "microsoft_teams",
    "webex",
    "zoom",
}


def check_create_meeting_recording_platform(value: str | None) -> CreateMeetingRecordingPlatform | None:
    if value is None:
        return None
    if value in CREATE_MEETING_RECORDING_PLATFORM_VALUES:
        return cast(CreateMeetingRecordingPlatform, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_MEETING_RECORDING_PLATFORM_VALUES!r}")
