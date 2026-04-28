from typing import Literal, cast

MeetingRecordingPlatform = Literal["google_meet", "microsoft_teams", "webex", "zoom"]

MEETING_RECORDING_PLATFORM_VALUES: set[MeetingRecordingPlatform] = {
    "google_meet",
    "microsoft_teams",
    "webex",
    "zoom",
}


def check_meeting_recording_platform(value: str | None) -> MeetingRecordingPlatform | None:
    if value is None:
        return None
    if value in MEETING_RECORDING_PLATFORM_VALUES:
        return cast(MeetingRecordingPlatform, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEETING_RECORDING_PLATFORM_VALUES!r}")
