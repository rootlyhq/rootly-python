from typing import Literal, cast

MeetingRecordingStatus = Literal["analyzing", "call_ended", "completed", "failed", "paused", "pending", "recording"]

MEETING_RECORDING_STATUS_VALUES: set[MeetingRecordingStatus] = {
    "analyzing",
    "call_ended",
    "completed",
    "failed",
    "paused",
    "pending",
    "recording",
}


def check_meeting_recording_status(value: str | None) -> MeetingRecordingStatus | None:
    if value is None:
        return None
    if value in MEETING_RECORDING_STATUS_VALUES:
        return cast(MeetingRecordingStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEETING_RECORDING_STATUS_VALUES!r}")
