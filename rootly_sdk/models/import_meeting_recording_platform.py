from typing import Literal, cast

ImportMeetingRecordingPlatform = Literal["google_meet", "microsoft_teams", "webex", "zoom"]

IMPORT_MEETING_RECORDING_PLATFORM_VALUES: set[ImportMeetingRecordingPlatform] = {
    "google_meet",
    "microsoft_teams",
    "webex",
    "zoom",
}


def check_import_meeting_recording_platform(value: str | None) -> ImportMeetingRecordingPlatform | None:
    if value is None:
        return None
    if value in IMPORT_MEETING_RECORDING_PLATFORM_VALUES:
        return cast(ImportMeetingRecordingPlatform, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IMPORT_MEETING_RECORDING_PLATFORM_VALUES!r}")
