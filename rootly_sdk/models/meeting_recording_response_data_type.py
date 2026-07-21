from typing import Literal, cast

MeetingRecordingResponseDataType = Literal["meeting_recordings"]

MEETING_RECORDING_RESPONSE_DATA_TYPE_VALUES: set[MeetingRecordingResponseDataType] = {
    "meeting_recordings",
}


def check_meeting_recording_response_data_type(value: str | None) -> MeetingRecordingResponseDataType | None:
    if value is None:
        return None
    if value in MEETING_RECORDING_RESPONSE_DATA_TYPE_VALUES:
        return cast(MeetingRecordingResponseDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEETING_RECORDING_RESPONSE_DATA_TYPE_VALUES!r}")
